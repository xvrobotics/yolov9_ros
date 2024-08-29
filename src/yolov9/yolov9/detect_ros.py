import rclpy
from rclpy.node import Node
import argparse
import os
import platform
import sys
from pathlib import Path
import torch
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
print(sys.path)
# Import YOLO-related modules
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLO root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, colorstr, cv2,
                           increment_path, non_max_suppression, scale_boxes, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, smart_inference_mode

class YOLOv9Node(Node):
    def __init__(self):
        super().__init__('yolov9_node')

        # Hardcoded Parameters
        # Declare ROS 2 Parameters
        self.declare_parameter('weights', '/home/xavi/High_Level1/src/yolov9/yolov9/gelan-c.pt')
        self.declare_parameter('source', '0')
        self.declare_parameter('data', '/home/xavi/High_Level1/src/yolov9/yolov9/data/coco128.yaml')
        self.declare_parameter('imgsz', [640, 640])
        self.declare_parameter('conf_thres', 0.7)
        self.declare_parameter('iou_thres', 0.45)
        self.declare_parameter('max_det', 1000)
        self.declare_parameter('device', '0')
        self.declare_parameter('view_img', False)
        self.declare_parameter('save_txt', False)
        self.declare_parameter('save_conf', False)
        self.declare_parameter('save_crop', False)
        self.declare_parameter('nosave', False)
        self.declare_parameter('classes', None)
        self.declare_parameter('agnostic_nms', False)
        self.declare_parameter('augment', False)
        self.declare_parameter('visualize', False)
        self.declare_parameter('update', False)
        self.declare_parameter('project', '/home/xavi/High_Level1/src/yolov9/yolov9/runs/detect')
        self.declare_parameter('name', 'exp')
        self.declare_parameter('exist_ok', False)
        self.declare_parameter('line_thickness', 3)
        self.declare_parameter('hide_labels', False)
        self.declare_parameter('hide_conf', False)
        self.declare_parameter('half', False)
        self.declare_parameter('dnn', False)
        self.declare_parameter('vid_stride', 1)
         # Initialize parameters
        self.get_params()
        
        # Create a timer to periodically update parameters
        self.timer = self.create_timer(1, self.get_params)  # 1 seconds interval
        #self.loader = LoadImagesFromFeed(img_size=640)
        self.subscription = self.create_subscription(
            Image,
            'vision/came/raw',  # Replace with your topic name
            self.camera_callback,
            10
        )
        self.subscription
        self.bridge = CvBridge()

    def get_params(self):
        self.weights = self.get_parameter('weights').get_parameter_value().string_value
        self.source = self.get_parameter('source').get_parameter_value().string_value
        self.data = self.get_parameter('data').get_parameter_value().string_value
        #self.imgsz = self.get_parameter('imgsz').get_parameter_value().integer_array_value
        self.conf_thres = self.get_parameter('conf_thres').get_parameter_value().double_value
        self.iou_thres = self.get_parameter('iou_thres').get_parameter_value().double_value
        self.max_det = self.get_parameter('max_det').get_parameter_value().integer_value
        self.device = self.get_parameter('device').get_parameter_value().string_value
        self.view_img = self.get_parameter('view_img').get_parameter_value().bool_value
        self.save_txt = self.get_parameter('save_txt').get_parameter_value().bool_value
        self.save_conf = self.get_parameter('save_conf').get_parameter_value().bool_value
        self.save_crop = self.get_parameter('save_crop').get_parameter_value().bool_value
        self.nosave = self.get_parameter('nosave').get_parameter_value().bool_value
        #self.classes = self.get_parameter('classes').get_parameter_value().integer_array_value
        self.agnostic_nms = self.get_parameter('agnostic_nms').get_parameter_value().bool_value
        self.augment = self.get_parameter('augment').get_parameter_value().bool_value
        self.visualize = self.get_parameter('visualize').get_parameter_value().bool_value
        self.update = self.get_parameter('update').get_parameter_value().bool_value
        self.project = self.get_parameter('project').get_parameter_value().string_value
        self.name = self.get_parameter('name').get_parameter_value().string_value
        self.exist_ok = self.get_parameter('exist_ok').get_parameter_value().bool_value
        self.line_thickness = self.get_parameter('line_thickness').get_parameter_value().integer_value
        self.hide_labels = self.get_parameter('hide_labels').get_parameter_value().bool_value
        self.hide_conf = self.get_parameter('hide_conf').get_parameter_value().bool_value
        self.half = self.get_parameter('half').get_parameter_value().bool_value
        self.dnn = self.get_parameter('dnn').get_parameter_value().bool_value
        self.vid_stride = self.get_parameter('vid_stride').get_parameter_value().integer_value
        self.classes = None  # Filter by class
        self.imgsz = [640, 640]  # Inference size h,w
        LOGGER.info("Getting params in ROS")
    def camera_callback(self, msg):
        self.get_logger().info('Received an image!')
        
        # Convert ROS Image message to OpenCV image
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f'Error converting image: {e}')
            return
        self.loader.add_image(cv_image)
        # Display the image using OpenCV
        for sources, im, im0, _, _ in self.loader:
            # Do something with the processed images
            # For example, show the image
            cv2.imshow('Processed Image', im[0].transpose((1, 2, 0)))  # Assuming single image in batch
            cv2.waitKey(1)  # Display image for 1ms
    @smart_inference_mode()
    def run(self):
        source = str(self.source)
        self.get_logger().info(f'source: {source}')
        save_img = not self.nosave and not source.endswith('.txt')  # save inference images
        self.get_logger().info(f'save_img: {save_img}')
        is_file = Path(source).suffix[1:] in (IMG_FORMATS + VID_FORMATS)
        self.get_logger().info(f'is_file: {is_file}')
        is_url = source.lower().startswith(('rtsp://', 'rtmp://', 'http://', 'https://'))
        self.get_logger().info(f'is_url: {is_url}')
        webcam = source.isnumeric() or source.endswith('.txt') or (is_url and not is_file)
        self.get_logger().info(f'webcam: {webcam}')
        screenshot = source.lower().startswith('screen')
        ros_topic = source.endswith('ros')
        self.get_logger().info(f'ros_topic: {ros_topic}')
        if is_url and is_file:
            source = check_file(source)  # download

        # Directories
        save_dir = increment_path(Path(self.project) / self.name, exist_ok=self.exist_ok)  # increment run
        (save_dir / 'labels' if self.save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

        # Load model
        device = select_device(self.device)
        self.get_logger().info(f'device: {device}')
        model = DetectMultiBackend(self.weights, device=device, dnn=self.dnn, data=self.data, fp16=self.half)
        stride, names, pt = model.stride, model.names, model.pt
        imgsz = check_img_size(self.imgsz, s=stride)  # check image size

        # Dataloader
        bs = 1  # batch_size
        if webcam:
            self.view_img = check_imshow(warn=True)
            dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=self.vid_stride)
            self.get_logger().info(f'dataset: {dataset}')
            bs = len(dataset)
        elif screenshot:
            dataset = LoadScreenshots(source, img_size=imgsz, stride=stride, auto=pt)
        elif ros_topic:
           # dataset = LoadImagesFromFeed
            self.get_logger().info(f'ROS OPTION!')
        else:
            dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=self.vid_stride)
        vid_path, vid_writer = [None] * bs, [None] * bs

        # Run inference
        model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup
        seen, windows, dt = 0, [], (Profile(), Profile(), Profile())
        for path, im, im0s, vid_cap, s in dataset:
            with dt[0]:
                im = torch.from_numpy(im).to(model.device)
                im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
                im /= 255  # 0 - 255 to 0.0 - 1.0
                if len(im.shape) == 3:
                    im = im[None]  # expand for batch dim

            # Inference
            with dt[1]:
                visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if self.visualize else False
                pred = model(im, augment=self.augment, visualize=visualize)

            # NMS
            with dt[2]:
                pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, self.classes, self.agnostic_nms, max_det=self.max_det)

            # Process predictions
            for i, det in enumerate(pred):  # per image
                seen += 1
                if webcam:  # batch_size >= 1
                    p, im0, frame = path[i], im0s[i].copy(), dataset.count
                    s += f'{i}: '
                else:
                    p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)

                p = Path(p)  # to Path
                save_path = str(save_dir / p.name)  # im.jpg
                txt_path = str(save_dir / 'labels' / p.stem) + ('' if dataset.mode == 'image' else f'_{frame}')  # im.txt
                s += '%gx%g ' % im.shape[2:]  # print string
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                imc = im0.copy() if self.save_crop else im0  # for save_crop
                annotator = Annotator(im0, line_width=self.line_thickness, example=str(names))
                if len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, 5].unique():
                        n = (det[:, 5] == c).sum()  # detections per class
                        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        if self.save_txt:  # Write to file
                            xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                            line = (cls, *xywh, conf) if self.save_conf else (cls, *xywh)  # label format
                            with open(f'{txt_path}.txt', 'a') as f:
                                f.write(('%g ' * len(line)).rstrip() % line + '\n')
                        if self.save_crop:  # Save crops
                            save_one_box(xyxy, imc, file=save_dir / 'crops' / names[int(cls)] / f'{p.stem}.jpg', BGR=True)
                        if self.view_img:  # Add bbox to image
                            c = int(cls)
                            label = None if self.hide_labels else (names[c] if self.hide_conf else f'{names[c]} {conf:.2f}')
                            annotator.box_label(xyxy, label, color=colors(c, True))

                # Print time (inference + NMS)
                #LOGGER.info(f"Done. ({dt[1].total / 1E3:.3f}s)")

                # Stream results
                im0 = annotator.result()
                if self.view_img:
                    if platform.system() == 'Linux' and p not in windows:
                        windows.append(p)
                        cv2.namedWindow(str(p), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
                        cv2.resizeWindow(str(p), im0.shape[1], im0.shape[0])
                    cv2.imshow(str(p), im0)
                    if cv2.waitKey(1) == ord('q'):  # q to quit
                        raise StopIteration

                # Save results (image)
                if save_img:
                    if platform.system() == 'Linux' and p not in windows:
                        windows.append(p)
                        cv2.namedWindow(str(p), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
                        cv2.resizeWindow(str(p), im0.shape[1], im0.shape[0])
                    cv2.imwrite(save_path, im0)

        # Print results
            LOGGER.info(f"{s}{'' if len(det) else '(no detections), '}{dt[1].dt * 1E3:.1f}ms")
        #LOGGER.info(f"Results saved to {colorstr('bold', save_dir)}")
        #LOGGER.info(f"Done. ({dt[0].total + dt[1].total + dt[2].total:.3f}s)")
        # Print results
        t = tuple(x.t / seen * 1E3 for x in dt)  # speeds per image
        LOGGER.info(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {(1, 3, *self.imgsz)}' % t)
        if self.save_txt or save_img:
            s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if self.save_txt else ''
            LOGGER.info(f"Results saved to {colorstr('bold', self.save_dir)}{s}")
        if self.update:
            strip_optimizer(self.weights[0])  # update model (to fix SourceChangeWarning)
        
def main(args=None):
    rclpy.init(args=args)
    node = YOLOv9Node()
    try:
        node.run()
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()

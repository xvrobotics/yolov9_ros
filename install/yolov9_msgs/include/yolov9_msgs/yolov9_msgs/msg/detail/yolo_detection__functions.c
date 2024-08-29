// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from yolov9_msgs:msg/YoloDetection.idl
// generated code does not contain a copyright notice
#include "yolov9_msgs/msg/detail/yolo_detection__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `class_name`
#include "rosidl_runtime_c/string_functions.h"

bool
yolov9_msgs__msg__YoloDetection__init(yolov9_msgs__msg__YoloDetection * msg)
{
  if (!msg) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__init(&msg->class_name)) {
    yolov9_msgs__msg__YoloDetection__fini(msg);
    return false;
  }
  // confidence
  // x_min
  // y_min
  // x_max
  // y_max
  // x_center
  // y_center
  return true;
}

void
yolov9_msgs__msg__YoloDetection__fini(yolov9_msgs__msg__YoloDetection * msg)
{
  if (!msg) {
    return;
  }
  // class_name
  rosidl_runtime_c__String__fini(&msg->class_name);
  // confidence
  // x_min
  // y_min
  // x_max
  // y_max
  // x_center
  // y_center
}

bool
yolov9_msgs__msg__YoloDetection__are_equal(const yolov9_msgs__msg__YoloDetection * lhs, const yolov9_msgs__msg__YoloDetection * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->class_name), &(rhs->class_name)))
  {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  // x_min
  if (lhs->x_min != rhs->x_min) {
    return false;
  }
  // y_min
  if (lhs->y_min != rhs->y_min) {
    return false;
  }
  // x_max
  if (lhs->x_max != rhs->x_max) {
    return false;
  }
  // y_max
  if (lhs->y_max != rhs->y_max) {
    return false;
  }
  // x_center
  if (lhs->x_center != rhs->x_center) {
    return false;
  }
  // y_center
  if (lhs->y_center != rhs->y_center) {
    return false;
  }
  return true;
}

bool
yolov9_msgs__msg__YoloDetection__copy(
  const yolov9_msgs__msg__YoloDetection * input,
  yolov9_msgs__msg__YoloDetection * output)
{
  if (!input || !output) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__copy(
      &(input->class_name), &(output->class_name)))
  {
    return false;
  }
  // confidence
  output->confidence = input->confidence;
  // x_min
  output->x_min = input->x_min;
  // y_min
  output->y_min = input->y_min;
  // x_max
  output->x_max = input->x_max;
  // y_max
  output->y_max = input->y_max;
  // x_center
  output->x_center = input->x_center;
  // y_center
  output->y_center = input->y_center;
  return true;
}

yolov9_msgs__msg__YoloDetection *
yolov9_msgs__msg__YoloDetection__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  yolov9_msgs__msg__YoloDetection * msg = (yolov9_msgs__msg__YoloDetection *)allocator.allocate(sizeof(yolov9_msgs__msg__YoloDetection), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(yolov9_msgs__msg__YoloDetection));
  bool success = yolov9_msgs__msg__YoloDetection__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
yolov9_msgs__msg__YoloDetection__destroy(yolov9_msgs__msg__YoloDetection * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    yolov9_msgs__msg__YoloDetection__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
yolov9_msgs__msg__YoloDetection__Sequence__init(yolov9_msgs__msg__YoloDetection__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  yolov9_msgs__msg__YoloDetection * data = NULL;

  if (size) {
    data = (yolov9_msgs__msg__YoloDetection *)allocator.zero_allocate(size, sizeof(yolov9_msgs__msg__YoloDetection), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = yolov9_msgs__msg__YoloDetection__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        yolov9_msgs__msg__YoloDetection__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
yolov9_msgs__msg__YoloDetection__Sequence__fini(yolov9_msgs__msg__YoloDetection__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      yolov9_msgs__msg__YoloDetection__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

yolov9_msgs__msg__YoloDetection__Sequence *
yolov9_msgs__msg__YoloDetection__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  yolov9_msgs__msg__YoloDetection__Sequence * array = (yolov9_msgs__msg__YoloDetection__Sequence *)allocator.allocate(sizeof(yolov9_msgs__msg__YoloDetection__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = yolov9_msgs__msg__YoloDetection__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
yolov9_msgs__msg__YoloDetection__Sequence__destroy(yolov9_msgs__msg__YoloDetection__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    yolov9_msgs__msg__YoloDetection__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
yolov9_msgs__msg__YoloDetection__Sequence__are_equal(const yolov9_msgs__msg__YoloDetection__Sequence * lhs, const yolov9_msgs__msg__YoloDetection__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!yolov9_msgs__msg__YoloDetection__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
yolov9_msgs__msg__YoloDetection__Sequence__copy(
  const yolov9_msgs__msg__YoloDetection__Sequence * input,
  yolov9_msgs__msg__YoloDetection__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(yolov9_msgs__msg__YoloDetection);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    yolov9_msgs__msg__YoloDetection * data =
      (yolov9_msgs__msg__YoloDetection *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!yolov9_msgs__msg__YoloDetection__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          yolov9_msgs__msg__YoloDetection__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!yolov9_msgs__msg__YoloDetection__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

# generated from rosidl_generator_py/resource/_idl.py.em
# with input from yolov9_msgs:msg/YoloDetection.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_YoloDetection(type):
    """Metaclass of message 'YoloDetection'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('yolov9_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'yolov9_msgs.msg.YoloDetection')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__yolo_detection
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__yolo_detection
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__yolo_detection
            cls._TYPE_SUPPORT = module.type_support_msg__msg__yolo_detection
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__yolo_detection

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class YoloDetection(metaclass=Metaclass_YoloDetection):
    """Message class 'YoloDetection'."""

    __slots__ = [
        '_class_name',
        '_confidence',
        '_x_min',
        '_y_min',
        '_x_max',
        '_y_max',
        '_x_center',
        '_y_center',
    ]

    _fields_and_field_types = {
        'class_name': 'string',
        'confidence': 'float',
        'x_min': 'float',
        'y_min': 'float',
        'x_max': 'float',
        'y_max': 'float',
        'x_center': 'float',
        'y_center': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.class_name = kwargs.get('class_name', str())
        self.confidence = kwargs.get('confidence', float())
        self.x_min = kwargs.get('x_min', float())
        self.y_min = kwargs.get('y_min', float())
        self.x_max = kwargs.get('x_max', float())
        self.y_max = kwargs.get('y_max', float())
        self.x_center = kwargs.get('x_center', float())
        self.y_center = kwargs.get('y_center', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.class_name != other.class_name:
            return False
        if self.confidence != other.confidence:
            return False
        if self.x_min != other.x_min:
            return False
        if self.y_min != other.y_min:
            return False
        if self.x_max != other.x_max:
            return False
        if self.y_max != other.y_max:
            return False
        if self.x_center != other.x_center:
            return False
        if self.y_center != other.y_center:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def class_name(self):
        """Message field 'class_name'."""
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'class_name' field must be of type 'str'"
        self._class_name = value

    @builtins.property
    def confidence(self):
        """Message field 'confidence'."""
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'confidence' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'confidence' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._confidence = value

    @builtins.property
    def x_min(self):
        """Message field 'x_min'."""
        return self._x_min

    @x_min.setter
    def x_min(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_min' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'x_min' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._x_min = value

    @builtins.property
    def y_min(self):
        """Message field 'y_min'."""
        return self._y_min

    @y_min.setter
    def y_min(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_min' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'y_min' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._y_min = value

    @builtins.property
    def x_max(self):
        """Message field 'x_max'."""
        return self._x_max

    @x_max.setter
    def x_max(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_max' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'x_max' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._x_max = value

    @builtins.property
    def y_max(self):
        """Message field 'y_max'."""
        return self._y_max

    @y_max.setter
    def y_max(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_max' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'y_max' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._y_max = value

    @builtins.property
    def x_center(self):
        """Message field 'x_center'."""
        return self._x_center

    @x_center.setter
    def x_center(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_center' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'x_center' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._x_center = value

    @builtins.property
    def y_center(self):
        """Message field 'y_center'."""
        return self._y_center

    @y_center.setter
    def y_center(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_center' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'y_center' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._y_center = value

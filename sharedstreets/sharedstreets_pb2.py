# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sharedstreets.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sharedstreets.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x13sharedstreets.proto\"\x1b\n\tDelimiter\x12\x0e\n\x06length\x18\x01 \x01(\r\"B\n\x12GISSectionMetadata\x12\x11\n\tsectionId\x18\x01 \x01(\t\x12\x19\n\x11sectionProperties\x18\x02 \x01(\t\"D\n\x0bGISMetadata\x12\x0e\n\x06source\x18\x01 \x01(\t\x12%\n\x08sections\x18\x02 \x03(\x0b\x32\x13.GISSectionMetadata\"\x8b\x01\n\nWaySection\x12\r\n\x05wayId\x18\x01 \x01(\x04\x12\x1d\n\troadClass\x18\x02 \x01(\x0e\x32\n.RoadClass\x12\x0e\n\x06oneWay\x18\x03 \x01(\x08\x12\x12\n\nroundabout\x18\x04 \x01(\x08\x12\x0c\n\x04link\x18\x05 \x01(\x08\x12\x0f\n\x07nodeIds\x18\x06 \x03(\x04\x12\x0c\n\x04name\x18\x07 \x01(\t\"=\n\x0bOSMMetadata\x12 \n\x0bwaySections\x18\x01 \x03(\x0b\x32\x0b.WaySection\x12\x0c\n\x04name\x18\x02 \x01(\t\"q\n\x15SharedStreetsMetadata\x12\x12\n\ngeometryId\x18\x01 \x01(\t\x12!\n\x0bosmMetadata\x18\x02 \x01(\x0b\x32\x0c.OSMMetadata\x12!\n\x0bgisMetadata\x18\x03 \x03(\x0b\x32\x0c.GISMetadata\"\xbe\x01\n\x15SharedStreetsGeometry\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1a\n\x12\x66romIntersectionId\x18\x02 \x01(\t\x12\x18\n\x10toIntersectionId\x18\x03 \x01(\t\x12\x1a\n\x12\x66orwardReferenceId\x18\x04 \x01(\t\x12\x17\n\x0f\x62\x61\x63kReferenceId\x18\x05 \x01(\t\x12\x1d\n\troadClass\x18\x06 \x01(\x0e\x32\n.RoadClass\x12\x0f\n\x07lonlats\x18\x07 \x03(\x01\"\xe9\x01\n\x11LocationReference\x12\x16\n\x0eintersectionId\x18\x01 \x01(\t\x12\x0b\n\x03lon\x18\x02 \x01(\x01\x12\x0b\n\x03lat\x18\x03 \x01(\x01\x12\x18\n\x0einboundBearing\x18\x04 \x01(\x05H\x00\x12\x19\n\x0foutboundBearing\x18\x05 \x01(\x05H\x01\x12\x1b\n\x11\x64istanceToNextRef\x18\x06 \x01(\x05H\x02\x42\x18\n\x16inboundBearing_presentB\x19\n\x17outboundBearing_presentB\x1b\n\x19\x64istanceToNextRef_present\"\xb5\x02\n\x16SharedStreetsReference\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ngeometryId\x18\x02 \x01(\t\x12\x34\n\tformOfWay\x18\x03 \x01(\x0e\x32!.SharedStreetsReference.FormOfWay\x12.\n\x12locationReferences\x18\x04 \x03(\x0b\x32\x12.LocationReference\"\x94\x01\n\tFormOfWay\x12\r\n\tUndefined\x10\x00\x12\x0c\n\x08Motorway\x10\x01\x12\x17\n\x13MultipleCarriageway\x10\x02\x12\x15\n\x11SingleCarriageway\x10\x03\x12\x0e\n\nRoundabout\x10\x04\x12\x11\n\rTrafficSquare\x10\x05\x12\x0c\n\x08SlipRoad\x10\x06\x12\t\n\x05Other\x10\x07\"\x8c\x01\n\x19SharedStreetsIntersection\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06nodeId\x18\x02 \x01(\x04\x12\x0b\n\x03lon\x18\x03 \x01(\x01\x12\x0b\n\x03lat\x18\x04 \x01(\x01\x12\x1b\n\x13inboundReferenceIds\x18\x05 \x03(\t\x12\x1c\n\x14outboundReferenceIds\x18\x06 \x03(\t*\x89\x01\n\tRoadClass\x12\x0c\n\x08Motorway\x10\x00\x12\t\n\x05Trunk\x10\x01\x12\x0b\n\x07Primary\x10\x02\x12\r\n\tSecondary\x10\x03\x12\x0c\n\x08Tertiary\x10\x04\x12\x0f\n\x0bResidential\x10\x05\x12\x10\n\x0cUnclassified\x10\x06\x12\x0b\n\x07Service\x10\x07\x12\t\n\x05Other\x10\x08\x42\x14\x42\x12SharedStreetsProtob\x06proto3')
)

_ROADCLASS = _descriptor.EnumDescriptor(
  name='RoadClass',
  full_name='RoadClass',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Motorway', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Trunk', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Primary', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Secondary', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Tertiary', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Residential', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unclassified', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Service', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Other', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1395,
  serialized_end=1532,
)
_sym_db.RegisterEnumDescriptor(_ROADCLASS)

RoadClass = enum_type_wrapper.EnumTypeWrapper(_ROADCLASS)
Motorway = 0
Trunk = 1
Primary = 2
Secondary = 3
Tertiary = 4
Residential = 5
Unclassified = 6
Service = 7
Other = 8


_SHAREDSTREETSREFERENCE_FORMOFWAY = _descriptor.EnumDescriptor(
  name='FormOfWay',
  full_name='SharedStreetsReference.FormOfWay',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Undefined', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Motorway', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MultipleCarriageway', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SingleCarriageway', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Roundabout', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TrafficSquare', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SlipRoad', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Other', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1101,
  serialized_end=1249,
)
_sym_db.RegisterEnumDescriptor(_SHAREDSTREETSREFERENCE_FORMOFWAY)


_DELIMITER = _descriptor.Descriptor(
  name='Delimiter',
  full_name='Delimiter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='length', full_name='Delimiter.length', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=50,
)


_GISSECTIONMETADATA = _descriptor.Descriptor(
  name='GISSectionMetadata',
  full_name='GISSectionMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sectionId', full_name='GISSectionMetadata.sectionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sectionProperties', full_name='GISSectionMetadata.sectionProperties', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=118,
)


_GISMETADATA = _descriptor.Descriptor(
  name='GISMetadata',
  full_name='GISMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='GISMetadata.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sections', full_name='GISMetadata.sections', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=188,
)


_WAYSECTION = _descriptor.Descriptor(
  name='WaySection',
  full_name='WaySection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wayId', full_name='WaySection.wayId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roadClass', full_name='WaySection.roadClass', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oneWay', full_name='WaySection.oneWay', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roundabout', full_name='WaySection.roundabout', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='WaySection.link', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeIds', full_name='WaySection.nodeIds', index=5,
      number=6, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='WaySection.name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=330,
)


_OSMMETADATA = _descriptor.Descriptor(
  name='OSMMetadata',
  full_name='OSMMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='waySections', full_name='OSMMetadata.waySections', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='OSMMetadata.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=332,
  serialized_end=393,
)


_SHAREDSTREETSMETADATA = _descriptor.Descriptor(
  name='SharedStreetsMetadata',
  full_name='SharedStreetsMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='geometryId', full_name='SharedStreetsMetadata.geometryId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osmMetadata', full_name='SharedStreetsMetadata.osmMetadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gisMetadata', full_name='SharedStreetsMetadata.gisMetadata', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=508,
)


_SHAREDSTREETSGEOMETRY = _descriptor.Descriptor(
  name='SharedStreetsGeometry',
  full_name='SharedStreetsGeometry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SharedStreetsGeometry.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fromIntersectionId', full_name='SharedStreetsGeometry.fromIntersectionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toIntersectionId', full_name='SharedStreetsGeometry.toIntersectionId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forwardReferenceId', full_name='SharedStreetsGeometry.forwardReferenceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backReferenceId', full_name='SharedStreetsGeometry.backReferenceId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roadClass', full_name='SharedStreetsGeometry.roadClass', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lonlats', full_name='SharedStreetsGeometry.lonlats', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=701,
)


_LOCATIONREFERENCE = _descriptor.Descriptor(
  name='LocationReference',
  full_name='LocationReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='intersectionId', full_name='LocationReference.intersectionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='LocationReference.lon', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat', full_name='LocationReference.lat', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inboundBearing', full_name='LocationReference.inboundBearing', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outboundBearing', full_name='LocationReference.outboundBearing', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distanceToNextRef', full_name='LocationReference.distanceToNextRef', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='inboundBearing_present', full_name='LocationReference.inboundBearing_present',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='outboundBearing_present', full_name='LocationReference.outboundBearing_present',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='distanceToNextRef_present', full_name='LocationReference.distanceToNextRef_present',
      index=2, containing_type=None, fields=[]),
  ],
  serialized_start=704,
  serialized_end=937,
)


_SHAREDSTREETSREFERENCE = _descriptor.Descriptor(
  name='SharedStreetsReference',
  full_name='SharedStreetsReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SharedStreetsReference.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='geometryId', full_name='SharedStreetsReference.geometryId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formOfWay', full_name='SharedStreetsReference.formOfWay', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locationReferences', full_name='SharedStreetsReference.locationReferences', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SHAREDSTREETSREFERENCE_FORMOFWAY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=940,
  serialized_end=1249,
)


_SHAREDSTREETSINTERSECTION = _descriptor.Descriptor(
  name='SharedStreetsIntersection',
  full_name='SharedStreetsIntersection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SharedStreetsIntersection.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='SharedStreetsIntersection.nodeId', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='SharedStreetsIntersection.lon', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat', full_name='SharedStreetsIntersection.lat', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inboundReferenceIds', full_name='SharedStreetsIntersection.inboundReferenceIds', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outboundReferenceIds', full_name='SharedStreetsIntersection.outboundReferenceIds', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1252,
  serialized_end=1392,
)

_GISMETADATA.fields_by_name['sections'].message_type = _GISSECTIONMETADATA
_WAYSECTION.fields_by_name['roadClass'].enum_type = _ROADCLASS
_OSMMETADATA.fields_by_name['waySections'].message_type = _WAYSECTION
_SHAREDSTREETSMETADATA.fields_by_name['osmMetadata'].message_type = _OSMMETADATA
_SHAREDSTREETSMETADATA.fields_by_name['gisMetadata'].message_type = _GISMETADATA
_SHAREDSTREETSGEOMETRY.fields_by_name['roadClass'].enum_type = _ROADCLASS
_LOCATIONREFERENCE.oneofs_by_name['inboundBearing_present'].fields.append(
  _LOCATIONREFERENCE.fields_by_name['inboundBearing'])
_LOCATIONREFERENCE.fields_by_name['inboundBearing'].containing_oneof = _LOCATIONREFERENCE.oneofs_by_name['inboundBearing_present']
_LOCATIONREFERENCE.oneofs_by_name['outboundBearing_present'].fields.append(
  _LOCATIONREFERENCE.fields_by_name['outboundBearing'])
_LOCATIONREFERENCE.fields_by_name['outboundBearing'].containing_oneof = _LOCATIONREFERENCE.oneofs_by_name['outboundBearing_present']
_LOCATIONREFERENCE.oneofs_by_name['distanceToNextRef_present'].fields.append(
  _LOCATIONREFERENCE.fields_by_name['distanceToNextRef'])
_LOCATIONREFERENCE.fields_by_name['distanceToNextRef'].containing_oneof = _LOCATIONREFERENCE.oneofs_by_name['distanceToNextRef_present']
_SHAREDSTREETSREFERENCE.fields_by_name['formOfWay'].enum_type = _SHAREDSTREETSREFERENCE_FORMOFWAY
_SHAREDSTREETSREFERENCE.fields_by_name['locationReferences'].message_type = _LOCATIONREFERENCE
_SHAREDSTREETSREFERENCE_FORMOFWAY.containing_type = _SHAREDSTREETSREFERENCE
DESCRIPTOR.message_types_by_name['Delimiter'] = _DELIMITER
DESCRIPTOR.message_types_by_name['GISSectionMetadata'] = _GISSECTIONMETADATA
DESCRIPTOR.message_types_by_name['GISMetadata'] = _GISMETADATA
DESCRIPTOR.message_types_by_name['WaySection'] = _WAYSECTION
DESCRIPTOR.message_types_by_name['OSMMetadata'] = _OSMMETADATA
DESCRIPTOR.message_types_by_name['SharedStreetsMetadata'] = _SHAREDSTREETSMETADATA
DESCRIPTOR.message_types_by_name['SharedStreetsGeometry'] = _SHAREDSTREETSGEOMETRY
DESCRIPTOR.message_types_by_name['LocationReference'] = _LOCATIONREFERENCE
DESCRIPTOR.message_types_by_name['SharedStreetsReference'] = _SHAREDSTREETSREFERENCE
DESCRIPTOR.message_types_by_name['SharedStreetsIntersection'] = _SHAREDSTREETSINTERSECTION
DESCRIPTOR.enum_types_by_name['RoadClass'] = _ROADCLASS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Delimiter = _reflection.GeneratedProtocolMessageType('Delimiter', (_message.Message,), dict(
  DESCRIPTOR = _DELIMITER,
  __module__ = 'sharedstreets_pb2'
  # @@protoc_insertion_point(class_scope:Delimiter)
  ))
_sym_db.RegisterMessage(Delimiter)

GISSectionMetadata = _reflection.GeneratedProtocolMessageType('GISSectionMetadata', (_message.Message,), dict(
  DESCRIPTOR = _GISSECTIONMETADATA,
  __module__ = 'sharedstreets_pb2'
  # @@protoc_insertion_point(class_scope:GISSectionMetadata)
  ))
_sym_db.RegisterMessage(GISSectionMetadata)

GISMetadata = _reflection.GeneratedProtocolMessageType('GISMetadata', (_message.Message,), dict(
  DESCRIPTOR = _GISMETADATA,
  __module__ = 'sharedstreets_pb2'
  # @@protoc_insertion_point(class_scope:GISMetadata)
  ))
_sym_db.RegisterMessage(GISMetadata)

WaySection = _reflection.GeneratedProtocolMessageType('WaySection', (_message.Message,), dict(
  DESCRIPTOR = _WAYSECTION,
  __module__ = 'sharedstreets_pb2'
  # @@protoc_insertion_point(class_scope:WaySection)
  ))
_sym_db.RegisterMessage(WaySection)

OSMMetadata = _reflection.GeneratedProtocolMessageType('OSMMetadata', (_message.Message,), dict(
  DESCRIPTOR = _OSMMETADATA,
  __module__ = 'sharedstreets_pb2'
  # @@protoc_insertion_point(class_scope:OSMMetadata)
  ))
_sym_db.RegisterMessage(OSMMetadata)

SharedStreetsMetadata = _reflection.GeneratedProtocolMessageType('SharedStreetsMetadata', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDSTREETSMETADATA,
  __module__ = 'sharedstreets_pb2'
  # @@protoc_insertion_point(class_scope:SharedStreetsMetadata)
  ))
_sym_db.RegisterMessage(SharedStreetsMetadata)

SharedStreetsGeometry = _reflection.GeneratedProtocolMessageType('SharedStreetsGeometry', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDSTREETSGEOMETRY,
  __module__ = 'sharedstreets_pb2'
  # @@protoc_insertion_point(class_scope:SharedStreetsGeometry)
  ))
_sym_db.RegisterMessage(SharedStreetsGeometry)

LocationReference = _reflection.GeneratedProtocolMessageType('LocationReference', (_message.Message,), dict(
  DESCRIPTOR = _LOCATIONREFERENCE,
  __module__ = 'sharedstreets_pb2'
  # @@protoc_insertion_point(class_scope:LocationReference)
  ))
_sym_db.RegisterMessage(LocationReference)

SharedStreetsReference = _reflection.GeneratedProtocolMessageType('SharedStreetsReference', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDSTREETSREFERENCE,
  __module__ = 'sharedstreets_pb2'
  # @@protoc_insertion_point(class_scope:SharedStreetsReference)
  ))
_sym_db.RegisterMessage(SharedStreetsReference)

SharedStreetsIntersection = _reflection.GeneratedProtocolMessageType('SharedStreetsIntersection', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDSTREETSINTERSECTION,
  __module__ = 'sharedstreets_pb2'
  # @@protoc_insertion_point(class_scope:SharedStreetsIntersection)
  ))
_sym_db.RegisterMessage(SharedStreetsIntersection)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\022SharedStreetsProto'))
# @@protoc_insertion_point(module_scope)
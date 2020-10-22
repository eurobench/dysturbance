//
// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

#pragma once

#include <stdint.h>

namespace OpcUa
{
enum class AttributeId : uint32_t
{
  NodeId = 1,
  NodeClass = 2,
  BrowseName = 3,
  DisplayName = 4,
  Description = 5,
  WriteMask = 6,
  UserWriteMask = 7,
  IsAbstract = 8,
  Symmetric = 9,
  InverseName = 10,
  ContainsNoLoops = 11,
  EventNotifier = 12,
  Value = 13,
  DataType = 14,
  ValueRank = 15,
  ArrayDimensions = 16,
  AccessLevel = 17,
  UserAccessLevel = 18,
  MinimumSamplingInterval = 19,
  Historizing = 20,
  Executable = 21,
  UserExecutable = 22,
  Unknown = ~uint32_t(),
};
} // namespace OpcUa


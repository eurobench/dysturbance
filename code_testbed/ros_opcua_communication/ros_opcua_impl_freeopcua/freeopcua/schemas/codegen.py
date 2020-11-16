
schema_files = dict(
  object_ids = 'NodeIds.csv',
  object_ids_tostring = 'NodeIds.csv',
  status_codes = 'StatusCode.csv',
  status_codes_tostring = 'StatusCode.csv',
  attribute_ids = 'AttributeIds.csv',
  attribute_ids_getoptionvalue = 'AttributeIds.csv',
  attribute_ids_tostring = 'AttributeIds.csv',
)

import csv
import re

def usage(msg=None):
  if msg: print ('Error {0}'.format(msg))
  print ('''Usage: {0} [cxx|py] [{1}]'''.format(sys.argv[0],','.join(schema_files.keys())))
  raise SystemExit


first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')
def camel_to_spacedstring(s):
  s1 = first_cap_re.sub(r'\1 \2', s)
  return all_cap_re.sub(r'\1 \2', s1).lower()


def cxx_object_ids(fname):
  print('''//
// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

#pragma once

#include <stdint.h>

namespace OpcUa
{
enum class ObjectId : uint32_t
{
  Null = 0,''')

  with open(fname) as fd:
    for e in csv.reader(fd, delimiter=','):
      print ('  {0} = {1},'.format(*e[:2]))

  print ('''};
}
''')

def cxx_object_ids_tostring(fname):
  print('''//
// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

#include <sstream>
#include <string>

#include "opc/ua/protocol/object_ids.h"

namespace OpcUa
{

std::string ToString(const ObjectId & value)
{
  switch (value)
  {''')

  with open(fname) as fd:
    for e in csv.reader(fd, delimiter=','):
      print ('''    case ObjectId::{0}:
      return "{1}";'''.format(e[0],e[0]))

  print ('''    default:
      {
        std::stringstream result;
        result << "unknown(" << static_cast<int>(value) << ")";
        return result.str();
      }
  }
}

} // namespace OpcUa
''')

def cxx_status_codes(fname):
  print('''//
// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

#pragma once

#include <stdint.h>

namespace OpcUa
{
enum class StatusCode : uint32_t
{
  Good = 0,''')

  with open(fname) as fd:
    for e in csv.reader(fd, delimiter=','):
      print ('  {0} = {1},'.format(*e[:2]))

  print ('''};

//raise appropriate exception if StatusCode is not Good
void CheckStatusCode(StatusCode code);

}
''')

def cxx_status_codes_tostring(fname):
  print('''//
// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

#include <string>
#include <sstream>
#include <iomanip>

#include "opc/ua/protocol/status_codes.h"

namespace OpcUa
{

std::string ToString(const StatusCode & code)
{
  if (code == StatusCode::Good)
    {
      return std::string();
    }

  std::stringstream stream;

  switch (code)
    {''')

  with open(fname) as fd:
    for e in csv.reader(fd, delimiter=','):
      print ('''    case StatusCode::{0}:
      stream << "{1}";
      break;
'''.format(e[0],e[2]))

  print ('''    default:
      stream << "Unknown StatusCode?";
      break;
    }

  stream << " (0x" << std::setfill('0') << std::setw(8) << std::hex << (unsigned)code << ")";

  return stream.str();
}

} // namespace OpcUa
''')

def cxx_attribute_ids(fname):
  print('''//
// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

#pragma once

#include <stdint.h>

namespace OpcUa
{
enum class AttributeId : uint32_t
{''')

  with open(fname) as fd:
    for e in csv.reader(fd, delimiter=','):
      print ('  {0} = {1},'.format(*e))

  print ('''  Unknown = ~uint32_t(),
};
} // namespace OpcUa
''')

def cxx_attribute_ids_getoptionvalue(fname):
  print('''//
// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

#pragma once

inline AttributeId GetAttributeIdOptionValue(const po::variables_map & vm)
{
  const std::string name = vm[OPTION_ATTRIBUTE].as<std::string>();
''')

  with open(fname) as fd:
    for e in csv.reader(fd, delimiter=','):
      print ('''  if (name == "{0}")
    {{
      return AttributeId::{1};
    }}
'''.format(camel_to_spacedstring(e[0]), e[0]))

  print ('''  throw std::logic_error(std::string("Unknown AttributeId: ") + name);
}
''')

def cxx_attribute_ids_tostring(fname):
  print('''//
// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

#include <sstream>
#include <string>

#include "opc/ua/protocol/attribute_ids.h"

namespace OpcUa
{

std::string ToString(const AttributeId & value)
{
  switch (value)
  {''')

  with open(fname) as fd:
    for e in csv.reader(fd, delimiter=','):
      print ('''    case AttributeId::{0}:
      return "{1}";'''.format(e[0],e[0]))

  print ('''    default:
      {
        std::stringstream result;
        result << "unknown(" << static_cast<int>(value) << ")";
        return result.str();
      }
  }
}

} // namespace OpcUa
''')

def py_object_ids(fname):
  print('''//
// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

#include <boost/python.hpp>

#include "opc/ua/protocol/object_ids.h"

using namespace boost::python;
using namespace OpcUa;

void py_opcua_enums_ObjectId()
{
  enum_<ObjectId>("ObjectId")
#define _value(X) value(#X, ObjectId:: X)''')

  with open(fname) as fd:
    for e in csv.reader(fd, delimiter=','):
      print ('  ._value({0})'.format(e[0]))

  print ('''#undef _value
  ;
}
''')

def py_status_codes(fname):
  print('''//
// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

#include <boost/python.hpp>

#include "opc/ua/protocol/status_codes.h"

using namespace boost::python;
using namespace OpcUa;

void py_opcua_enums_StatusCode()
{
  enum_<StatusCode>("StatusCode")
#define _value(X) value(#X, StatusCode:: X)''')

  with open(fname) as fd:
    for e in csv.reader(fd, delimiter=','):
      print ('  ._value({0})'.format(e[0]))

  print ('''#undef _value
  ;
}
''')

def py_status_codes_tostring(fname):
  raise Exception('py_status_codes_tostring not implemented')

def py_attribute_ids(fname):
  print('''//
// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

#include <boost/python.hpp>

#include "opc/ua/protocol/attribute_ids.h"

using namespace boost::python;
using namespace OpcUa;

void py_opcua_enums_AttributeId()
{
  enum_<AttributeId>("AttributeId")
#define _value(X) value(#X, AttributeId:: X)''')

  with open(fname) as fd:
    for e in csv.reader(fd, delimiter=','):
      print ('  ._value({0})'.format(e[0]))

  print ('''#undef _value
  ;
}
''')

def py_attribute_ids_getoptionvalue(fname):
  raise Exception('py_attribute_ids_getoptionvalue not implemented')

if __name__ == '__main__':
  import sys
  import os
  if len(sys.argv) != 3: usage()
  target, what = sys.argv[1:]
  if target not in ('cxx','py',): usage()
  if what not in schema_files.keys(): usage()
  call='{0}_{1}'.format(target,what)
  try:
    relpath = os.path.dirname(__file__)
    locals()[call](os.path.join(relpath,schema_files[what]))
  except Exception as e:
    usage(e)


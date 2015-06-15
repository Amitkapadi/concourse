#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Operator:
  """
  Enumerates the list of operators that can be used in criteria specifications.
  """
  REGEX = 1
  NOT_REGEX = 2
  EQUALS = 3
  NOT_EQUALS = 4
  GREATER_THAN = 5
  GREATER_THAN_OR_EQUALS = 6
  LESS_THAN = 7
  LESS_THAN_OR_EQUALS = 8
  BETWEEN = 9
  LINKS_TO = 10
  LIKE = 11
  NOT_LIKE = 12

  _VALUES_TO_NAMES = {
    1: "REGEX",
    2: "NOT_REGEX",
    3: "EQUALS",
    4: "NOT_EQUALS",
    5: "GREATER_THAN",
    6: "GREATER_THAN_OR_EQUALS",
    7: "LESS_THAN",
    8: "LESS_THAN_OR_EQUALS",
    9: "BETWEEN",
    10: "LINKS_TO",
    11: "LIKE",
    12: "NOT_LIKE",
  }

  _NAMES_TO_VALUES = {
    "REGEX": 1,
    "NOT_REGEX": 2,
    "EQUALS": 3,
    "NOT_EQUALS": 4,
    "GREATER_THAN": 5,
    "GREATER_THAN_OR_EQUALS": 6,
    "LESS_THAN": 7,
    "LESS_THAN_OR_EQUALS": 8,
    "BETWEEN": 9,
    "LINKS_TO": 10,
    "LIKE": 11,
    "NOT_LIKE": 12,
  }

class Type:
  """
  Enumerates the possible TObject types
  """
  BOOLEAN = 1
  DOUBLE = 2
  FLOAT = 3
  INTEGER = 4
  LONG = 5
  LINK = 6
  STRING = 7
  TAG = 8
  NULL = 9

  _VALUES_TO_NAMES = {
    1: "BOOLEAN",
    2: "DOUBLE",
    3: "FLOAT",
    4: "INTEGER",
    5: "LONG",
    6: "LINK",
    7: "STRING",
    8: "TAG",
    9: "NULL",
  }

  _NAMES_TO_VALUES = {
    "BOOLEAN": 1,
    "DOUBLE": 2,
    "FLOAT": 3,
    "INTEGER": 4,
    "LONG": 5,
    "LINK": 6,
    "STRING": 7,
    "TAG": 8,
    "NULL": 9,
  }

class Diff:
  ADDED = 1
  REMOVED = 2

  _VALUES_TO_NAMES = {
    1: "ADDED",
    2: "REMOVED",
  }

  _NAMES_TO_VALUES = {
    "ADDED": 1,
    "REMOVED": 2,
  }


class AccessToken:
  """
  A temporary token that is returned by the
  {@link ConcourseService#login(String, String)} method to grant access
  to secure resources in place of raw credentials.

  Attributes:
   - data
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'data', None, None, ), # 1
  )

  def __init__(self, data=None,):
    self.data = data

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.data = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AccessToken')
    if self.data is not None:
      oprot.writeFieldBegin('data', TType.STRING, 1)
      oprot.writeString(self.data)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.data is None:
      raise TProtocol.TProtocolException(message='Required field data is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.data)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TransactionToken:
  """
  A token that identifies a Transaction.

  Attributes:
   - accessToken
   - timestamp
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'accessToken', (AccessToken, AccessToken.thrift_spec), None, ), # 1
    (2, TType.I64, 'timestamp', None, None, ), # 2
  )

  def __init__(self, accessToken=None, timestamp=None,):
    self.accessToken = accessToken
    self.timestamp = timestamp

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.accessToken = AccessToken()
          self.accessToken.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.timestamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TransactionToken')
    if self.accessToken is not None:
      oprot.writeFieldBegin('accessToken', TType.STRUCT, 1)
      self.accessToken.write(oprot)
      oprot.writeFieldEnd()
    if self.timestamp is not None:
      oprot.writeFieldBegin('timestamp', TType.I64, 2)
      oprot.writeI64(self.timestamp)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.accessToken is None:
      raise TProtocol.TProtocolException(message='Required field accessToken is unset!')
    if self.timestamp is None:
      raise TProtocol.TProtocolException(message='Required field timestamp is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.accessToken)
    value = (value * 31) ^ hash(self.timestamp)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TSecurityException(TException):
  """
  The security ex that occurs when the user session
  is invalidated from Concourse server.

  Attributes:
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TSecurityException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TTransactionException(TException):
  """
  The exception that is thrown from the server when a
  transaction related exception occurs.
  """

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TTransactionException')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TParseException(TException):
  """
  The exception that is thrown from the server when an
  error occurs while parsing a string.

  Attributes:
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TParseException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

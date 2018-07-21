-- thanks to https://mika-s.github.io/wireshark/lua/dissector/2017/11/04/creating-a-wireshark-dissector-in-lua-1.html

myproto_protocol = Proto("MYPROTO",  "MYPROTO Protocol")
myproto_protocol_port = 7777

-- protocol fields
-- ProtoField.new(name, abbr, type, [valuestring], [base], [mask], [descr])
-- name: Actual name of the field (the string that appears in the tree).
-- abbr: Filter name of the field (the string that is used in filters).
-- type: one of: ftypes.BOOLEAN, ftypes.UINT8, ftypes.UINT16, ftypes.UINT24, ftypes.UINT32, ftypes.UINT64, ftypes.INT8, ftypes.INT16, ftypes.INT24, ftypes.INT32, ftypes.INT64, ftypes.FLOAT, ftypes.DOUBLE , ftypes.ABSOLUTE_TIME, ftypes.RELATIVE_TIME, ftypes.STRING, ftypes.STRINGZ, ftypes.UINT_STRING, ftypes.ETHER, ftypes.BYTES, ftypes.UINT_BYTES, ftypes.IPv4, ftypes.IPv6, ftypes.IPXNET, ftypes.FRAMENUM, ftypes.PCRE, ftypes.GUID, ftypes.OID, ftypes.PROTOCOL, ftypes.REL_OID, ftypes.SYSTEM_ID, ftypes.EUI64 or ftypes.NONE.
-- base: one of: base.NONE, base.DEC, base.HEX, base.OCT, base.DEC_HEX, base.HEX_DEC or base.UNIT_STRING.

--             create a field.   label in filter settings, label in the subtree, display as decimal
--payload = ProtoField.int32("myproto.message_length", "messageLength", base.DEC)
--                                                                         base.ASCII or base.UNICODE
header = ProtoField.string("myproto.message_header", "messageHeader", base.ASCII)
data = ProtoField.string("myproto.message_data", "messageData", base.ASCII)

-- add to the protocol fields
myproto_protocol.fields = {header, data}

function myproto_protocol.dissector(buffer, pinfo, tree)
  length = buffer:len()
  if length == 0 then return end

  -- display column name 
  pinfo.cols.protocol = myproto_protocol.name

  -- display this text instead of Data in Wireshark
  local subtree = tree:add(myproto_protocol, buffer(), "MYPROTO Protocol Data")
  
  -- add_le = little endian (big endian is only add)
  subtree:add_le(header, buffer(0,4))
  subtree:add_le(data, buffer(4,4))
  
end

-- here it is assigned to some proto and port
local udp_port = DissectorTable.get("udp.port")
udp_port:add(myproto_protocol_port, myproto_protocol)














# import requests
# import base64


# url = "http://192.168.246.140:8080/api/devices/9c65f92106030104/queue"
# a = '5A0B030200090A2391'
# print(a)
# a = bytes.fromhex(a)
# print(a)
# # a = "aaa"
# # c = struct.pack('Q', a)
# # print("c:", c)
# # exit(0)
# b = base64.b64encode(a)
# b = str(b,'utf-8')
# print(b)
# # b = base64.b64decode(b)
# # # c = b.hex()
# # print(b)
# # exit(0)
# print(b)
# api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5X2lkIjoiM2I2YTJkOGEtNzBlMC00ZDdjLWFhZjAtYTZmNGIzMGE4MDc2IiwiYXVkIjoiYXMiLCJpc3MiOiJhcyIsIm5iZiI6MTY2NjUzNzQ1MSwic3ViIjoiYXBpX2tleSJ9.b-VlNYuRRgFTR4jTTQ9gB_FuhADlWi0-kI31ta06ZNE"
# payload = '{"deviceQueueItem": {"confirmed": False,"data": b,"fPort": 10}}'
# header = {"Content-Type": "application/json",
#         "Accept": "application/json",
#         "Grpc-Metadata-Authorization": api_token}
# responses = requests.post(url=url, data=payload, headers=header)
# print(responses.text)

# import os
# import sys

# import grpc
# from chirpstack_api import api

# # Configuration.

# # This must point to the API interface.
# server = "192.168.246.140:8080"

# # The DevEUI for which you want to enqueue the downlink.
# dev_eui = "9c65f92106030104"

# # The API token (retrieved using the web-interface).
# api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5X2lkIjoiZTQxNTNlOGYtYTE0NC00ZTQ0LWI5M2EtMGIxY2YwY2FlMmFhIiwiYXVkIjoiYXMiLCJpc3MiOiJhcyIsIm5iZiI6MTY2NjUzNDI0OCwic3ViIjoiYXBpX2tleSJ9.Evuo6hgg9tKTkekWjZx3dsJ4WceOkuH7xPApTrZYlNs"

# if __name__ == "__main__":
#   # Connect without using TLS.
#   channel = grpc.insecure_channel(server)

#   # Device-queue API client.
#   client = api.DeviceServiceStub(channel)

#   # Define the API key meta-data.
#   auth_token = [("authorization", "Bearer %s" % api_token)]

#   # Construct request.
#   req = api.EnqueueDeviceQueueItemRequest()
#   req.queue_item.confirmed = False
#   req.queue_item.data = bytes([0x01, 0x02, 0x03])
#   req.queue_item.dev_eui = dev_eui
#   req.queue_item.f_port = 10

#   resp = client.Enqueue(req, metadata=auth_token)

#   # Print the downlink id
#   print(resp.id)


import os
import sys

import grpc
from chirpstack_api.as_pb.external import api

# Configuration.

# This must point to the API interface.
server = "192.168.246.140:8080"

# The DevEUI for which you want to enqueue the downlink.
dev_eui = bytes([0x9c, 0x65, 0xf9, 0x21, 0x06, 0x03, 0x01, 0x04])

# The API token (retrieved using the web-interface).
# api_token = "..."
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5X2lkIjoiYjhhMzAxYzItZTljMi00NjAyLWE4MWUtZjRjYjVlNmJiYTQ1IiwiYXVkIjoiYXMiLCJpc3MiOiJhcyIsIm5iZiI6MTY2NjU2OTg2Niwic3ViIjoiYXBpX2tleSJ9.Rvh0Ar4C_YuxDb-OH2HdBdo4k1uiUI6U4_IQC7YjJL4"

if __name__ == "__main__":
  # Connect without using TLS.
  channel = grpc.insecure_channel(server)

  # Device-queue API client.
  client = api.DeviceQueueServiceStub(channel)

  # Define the API key meta-data.
  auth_token = [("authorization", "Bearer %s" % api_token)]

  # Construct request.
  req = api.EnqueueDeviceQueueItemRequest()
  req.device_queue_item.confirmed = False
  req.device_queue_item.data = bytes([0x5a, 0x0b, 0x06, 0x06, 0x00, 0x21, 0x04, 0x10, 0x0e, 0x00, 0x00, 0x6e, 0x20])
  req.device_queue_item.dev_eui = dev_eui.hex()
  req.device_queue_item.f_port = 10

  resp = client.Enqueue(req, metadata=auth_token)

  # Print the downlink frame-counter value.
  print(resp.f_cnt)
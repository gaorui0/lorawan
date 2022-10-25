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

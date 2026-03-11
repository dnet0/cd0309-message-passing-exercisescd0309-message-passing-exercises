import time
from concurrent import futures

import grpc
import item_pb2
import item_pb2_grpc
import order_pb2
import order_pb2_grpc

class ItemServicer(item_pb2_grpc.ItemServiceServicer):
    def Create(self, request, context):

        request_value = {
            "name": request.name,
            "brand_name": request.brand_name,
            "id": int(request.id),
            "weight": request.weight,
        }
        print(request_value)

        return item_pb2.ItemMessage(**request_value)

class OrderServicer(order_pb2_grpc.OrderServiceServicer):
    def Create(self, request, context):
        request_value = {
            "id" : request.id,
            "created_by" : request.created_by,
            "status" : request.status,
            "created_at" : request.created_at,
            "equipment" : ["KEYBOARD"]
        }
        print(request_value)
        return order_pb2.OrderMessage(**request_value)
    def Get(self, request, context):
        result = order_pb2.OrderMessageList()
        order = order_pb2.OrderMessage(
            id="123",
            created_by="system",
            status=order_pb2.OrderMessage.Status.QUEUED,
            created_at="2026-03-11",
            equipment=[order_pb2.OrderMessage.Equipment.MOUSE]
        )

        result.orders.extend([order])
        return result

# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
item_pb2_grpc.add_ItemServiceServicer_to_server(ItemServicer(), server)
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

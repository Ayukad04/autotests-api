import grpc

import course_service_pb2
import course_service_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = course_service_pb2_grpc.CourseServiceStub(channel)

    response = stub.GetCourse(
        course_service_pb2.GetCourseRequest(course_id="api-course")
    )

    print(response)


if __name__ == "__main__":
    run()
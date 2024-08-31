import aws_cdk as core
import aws_cdk.assertions as assertions

from 03_web_page_with_db.03_web_page_with_db_stack import 03WebPageWithDbStack

# example tests. To run these tests, uncomment this file along with the example
# resource in 03_web_page_with_db/03_web_page_with_db_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 03WebPageWithDbStack(app, "03-web-page-with-db")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

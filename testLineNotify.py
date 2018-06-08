import os
import lineTool

# token = os.environ["LINE_TEST_TOKEN"]
token = "ThkCHuhjQlG0DsIN8S0LlbIEAwlAvoHZ8WvpNNVJ6SS"
msg = "Hello world"


lineTool.lineNotify(token, msg)
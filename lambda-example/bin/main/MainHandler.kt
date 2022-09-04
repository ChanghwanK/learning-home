import com.amazonaws.services.lambda.runtime.Context
import com.amazonaws.services.lambda.runtime.RequestHandler
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent
import com.google.gson.Gson
import dto.TestResponse

class MainHandler: RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    val gson = Gson()

    override fun handleRequest(
        input: APIGatewayProxyRequestEvent,
        context: Context
    ): APIGatewayProxyResponseEvent {
        val header = mutableMapOf<String, String>()
        header["Content-Type"] = "application/json"
        val response = APIGatewayProxyResponseEvent().withHeaders(header)

        response.statusCode = 200
        response.body = gson.toJson(TestResponse("Hello World"))

        return response
    }
}
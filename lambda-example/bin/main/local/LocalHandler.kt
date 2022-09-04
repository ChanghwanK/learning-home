package local
import MainHandler
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent

fun main() {
    val handler = MainHandler()
    val request = APIGatewayProxyRequestEvent()
    val context = LocalContext()
    val response = handler.handleRequest(request, context)
    println("Response Body: ${response.body})")
}
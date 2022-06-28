package entity
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbAttribute
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbBean
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbPartitionKey
import java.time.LocalDateTime

@DynamoDbBean
data class Event (
    @get:DynamoDbPartitionKey
    var id: String,
    var title: String,
    var createdAt: LocalDateTime
)
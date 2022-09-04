package storage

import entity.Event
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient
import software.amazon.awssdk.enhanced.dynamodb.TableSchema
import software.amazon.awssdk.regions.Region
import software.amazon.awssdk.services.dynamodb.DynamoDbClient

class DynamoDBStorage(
    region: Region
) {
    private val dbClient = DynamoDbClient.builder()
        .region(region)
        .build()
    private val enhancedDBClient = DynamoDbEnhancedClient.builder()
        .dynamoDbClient(dbClient)
        .build()

    fun getAppDao(): EventEntityDao {
        val table = enhancedDBClient.table(
            EventEntityDao.Table_NAME,
            TableSchema.fromClass(Event::class.java)
        )

        return EventEntityDao(table)
    }
}
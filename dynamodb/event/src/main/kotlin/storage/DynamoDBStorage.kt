package storage

import entity.Event
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient
import software.amazon.awssdk.enhanced.dynamodb.TableSchema
import software.amazon.awssdk.regions.Region
import software.amazon.awssdk.services.dynamodb.DynamoDbClient

class DynamoDBStorage(
    region: Region
) {
    private val dbClient = DynamoDbClient.builder().region(region).build()
    private val enhancedDBClient = DynamoDbEnhancedClient.builder()
        .dynamoDbClient(dbClient)
        .build()

    /**
     * return Dao
     */
    fun getAppDao(): EventEntityDao {
        val table = enhancedDBClient.table(
            EventEntityDao.Table_NAME,
            TableSchema.fromClass(Event::class.java)
        )
        return EventEntityDao(table)
    }

    /**
     * TODO
     *  밥 먹고 와서
     *  - readme 추가
     *  - dynamodb 접근 (Entity 설계, Insert 등등)
     *
     *  Research
     *  -  dynamodb sdk 종류가 다 다른가?
     */

}
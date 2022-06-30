package storage

import entity.Event
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable
import software.amazon.awssdk.enhanced.dynamodb.Key


class EventEntityDao(private val table: DynamoDbTable<Event>) {
    companion object {
        const val Table_NAME = "event"
    }

    fun insert(value: Event) {
        table.putItem(value)
    }

    fun read(id: String): Event? {
        val key = Key.builder()
            .partitionValue(id)
            .build()
        return table.getItem(key)
    }

}
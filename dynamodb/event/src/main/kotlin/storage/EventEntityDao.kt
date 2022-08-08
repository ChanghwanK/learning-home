package storage

import entity.Event
import software.amazon.awssdk.core.pagination.sync.SdkIterable
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable
import software.amazon.awssdk.enhanced.dynamodb.Expression
import software.amazon.awssdk.enhanced.dynamodb.Key
import software.amazon.awssdk.enhanced.dynamodb.model.Page
import software.amazon.awssdk.enhanced.dynamodb.model.ScanEnhancedRequest
import software.amazon.awssdk.services.dynamodb.model.AttributeValue
import java.util.StringJoiner


class EventEntityDao(private val table: DynamoDbTable<Event>) {
    companion object {
        const val Table_NAME = "event"
    }

    fun insert(value: Event) {
        table.putItem(value)
    }

    fun read(id: String, sortedKey: String): Event? {
        val key = Key.builder()
            .partitionValue(id)
            .sortValue(sortedKey)
            .build()
        return table.getItem(key)
    }

//    fun scanByExpression(eventNames: MutableList<String>): SdkIterable<Event>? {
////        [ {"S": "Cookies"} , {"S": "Coffee"}, {"N": "3.14159"}]
//
//        val attrValues: MutableMap<String, AttributeValue> = HashMap()
//        attrValues["eventName"] = AttributeValue.builder().ns(eventNames).build()
//        val expression = Expression.builder()
//            .expressionValues(attrValues)
//            .expression("In(eventName :eventName)")
//            .build()
//
//        val request = ScanEnhancedRequest.builder()
//            .filterExpression(expression)
//            .build()
//
//        return table.scan(request).items()
//    }

//    val attrValues: MutableMap<String, AttributeValue> = HashMap()
//    attrValues[":country"] = AttributeValue.builder().s(country).build()

//    fun testScan(eventName: String): SdkIterable<Event>? {
//        val attrValues: MutableMap<String, AttributeValue> = HashMap()
//        attrValues["eventName"] = AttributeValue.builder().s(eventName).build()
//        val expression = Expression.builder()
//            .expressionValues(attrValues)
//            .expression("contains(#eventNames, :eventName)")
//            .build()
//
//        val request = ScanEnhancedRequest.builder()
//            .filterExpression(expression)
//            .build()
//
//        return table.scan(request).items()
//    }

    //    fun testScan(eventName: String): SdkIterable<Event>? {
//        val attrValues: MutableMap<String, AttributeValue> = HashMap()
//        attrValues[":eventName"] = AttributeValue.builder().s(eventName).build()
//        val expression = Expression.builder()
//            .expressionValues(attrValues)
//            .expression("eventName IN (:eventName)")
//            .build()
//
//        val request = ScanEnhancedRequest.builder()
//            .filterExpression(expression)
//            .build()
//
//        return table.scan(request).items()
//    }
    fun testScan(eventNames: List<String>): SdkIterable<Event>? {
        val attrValues: MutableMap<String, AttributeValue> = HashMap()
        attrValues[":eventNames"] = AttributeValue.builder().ss(eventNames).build()
        val expression = Expression.builder()
            .expressionValues(attrValues)
            .expression("eventName IN (:eventNames)")
            .build()
        

        println("expression >>>> ${expression.expression()}")
        println("expression >>>> ${expression.expressionValues()}")


        val request = ScanEnhancedRequest.builder()
            .filterExpression(expression)
            .build()

        return table.scan(request).items()
    }

    fun test2(eventNames: List<String>): SdkIterable<Event>? {
        val attrValues: MutableMap<String, AttributeValue> = HashMap()
        var index = 0
        eventNames.forEach {
            index++
            val key = ":eventName$index"
            attrValues[key] = AttributeValue.builder().s(it).build()
        }

        println("attr >>>> $attrValues")
        println("==========================================================")

//        println("data >>> ${attrValues.keys.joinToString(",") { key }}")

        val expression = Expression.builder()
            .expressionValues(attrValues)
            .expression("eventName IN (${attrValues.keys.joinToString(",") { it }})")
            .build()

        val request = ScanEnhancedRequest.builder()
            .filterExpression(expression)
            .build()

        return table.scan(request).items()
    }
    fun createDynamoDBQueryExpression(eventNames: List<String>): String {
        val eventNamesString = eventNames.joinToString(" ")
        return "eventName IN ($eventNamesString)"
    }
}
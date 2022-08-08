import entity.Event
import software.amazon.awssdk.regions.Region
import storage.DynamoDBStorage

fun main() {
    val region = Region.of("ap-northeast-2")
    val dbStorage = DynamoDBStorage(region = region)
    val dao = dbStorage.getAppDao()

//    val entity = Event.toEntity("AB", "1", "PUSH",  "사과입니다.")
//
//    val entity2 = Event.toEntity("AB-123", "2", "PUSH",  "사과입니다1.")
//    val entity3 = Event.toEntity("AB-435", "3", "OPEN",  "OPEN 입니다2.")
//    val entity4 = Event.toEntity("AB-124", "4", "OPEN",  "OPEN 입니다3.")
//    val entity5 = Event.toEntity("AB-532", "5", "PUSH",  "사과입니다4.")
//    dao.insert(entity)
//    dao.insert(entity2)
//    dao.insert(entity3)
//    dao.insert(entity4)
//    dao.insert(entity5)

//    println("read")
//
//    dao.scanByExpression(mutableListOf("PUSH", "OPEN"))?.forEach {
//        println(it)
//    }
    dao.test2(listOf("PUSH", "OPEN"))?.forEach{
        println(it)
    }
//    dao.testScan(listOf("PUSH", "OPEN"))?.forEach {
//        println(it)
//    }
}


fun dynamodbTest() {
//    val ddb = AmazonDynamoDBClientBuilder.standard()
//        .withRegion(Regions.AP_NORTHEAST_2)
//        .build()
}

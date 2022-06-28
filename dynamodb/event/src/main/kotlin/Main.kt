import entity.Event
import software.amazon.awssdk.regions.Region
import storage.DynamoDBStorage
import java.rmi.activation.ActivationGroupDesc.CommandEnvironment
import java.time.LocalDateTime

fun main() {
    val date = LocalDateTime.now()
    val region = Region.of("ap-northeast-2")
    val dbStorage = DynamoDBStorage(region = region)
    val dao = dbStorage.getAppDao()
    val entity = Event(
        id = "test-1",
        title = "test title-1"
    )
//    print(entity)
    println("Insert Start")
    dao.insert(entity)

}


import entity.Event
import software.amazon.awssdk.regions.Region
import storage.DynamoDBStorage
import java.rmi.activation.ActivationGroupDesc.CommandEnvironment
import java.time.LocalDateTime

fun main() {
    val region = Region.of("ap-northeast-2")
    val dbStorage = DynamoDBStorage(region = region)
    val dao = dbStorage.getAppDao()

    val entity = Event.toEntity("Test-01", "Test 입니다.")
    dao.insert(entity)
    val data = dao.read("test-01")
    println("data >>> $data")
}


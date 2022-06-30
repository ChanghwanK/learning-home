import entity.Event
import software.amazon.awssdk.regions.Region
import storage.DynamoDBStorage
import java.rmi.activation.ActivationGroupDesc.CommandEnvironment
import java.time.LocalDateTime

fun main() {
    val region = Region.of("ap-northeast-2")
    val dbStorage = DynamoDBStorage(region = region)
    val dao = dbStorage.getAppDao()

    dao.insert(Event.toEntity("Test-03", "Test 입니다."))
}


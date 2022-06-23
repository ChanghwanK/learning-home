### Overview
- SAM App toml 변경에 따라 새로운 stack이 뜨는지 검증하기 위한 Study 입니다.

### Goals
- 기존 SAM App을 복사해서 toml을 바꿨을 때, Lambda Function에 영향이 있는지를 검증하는 것이 목표  

### Test List
1. sam app을 만들고 배포 후 sam-app-2로 복사한 뒤 toml을 바꿨을 때 기존 람다와는 무관하게 새로운 Function이 뜨는가?
2. 기존 sam app에서 그냥 toml을 바꿨을 땐 어떻게 변경되는가?


### Result
> sam app을 만들고 배포 후 sam-app-2로 복사한 뒤 toml을 바꿨을 때 기존 람다와는 무관하게 새로운 Function이 뜨는가?

- 기존 sam app과는 무관하게 새롭게 뜸

<br>

> 기존 sam app에서 그냥 toml을 바꿨을 땐 어떻게 변경되는가?
- toml을 수정했을 때 sam build 하면 새로운 sam app이 생기는 것과 동일
- 따라서 `sam deploy --guided` 명령어를 입력해야 함 
- 즉, 새로운 Function이 뜨는 것


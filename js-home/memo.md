### 목표
- 한 chart의 APK 개수만큼 저장이 되어야 함
- 이전 방식은 모든 apk 정보가 appendRow의 csvs에 들어있다보니 한 라인에 쭉 들어감
- 따라서 append row를 apk 정보가만큼 call해서 한 라인에 한개씩 들어가는 것이 목표

로직
1. csv 라는 변수에 줄 바꿈을 기준으로 APK 정보가 Split 되어 있음 => 총 N개의 APK 정보
2. N개의 APK 정보를 데이터 전처리 실시함
3. 전처리 된 데이터를 새로운 Array에 담음
4. Array 길이만큼 돌면서 append row 하면 좋을 듯


정리 - 1
- appendRow를 apk 개수만큼 호출해야 함
- 따라서 appendRow에 들어갈 데이터들을 잘 제공해주는 것이 중요
- appnedRow의 데이터는 ['package', 'developer'] 등등과 같은 전처리된 data들


각 함수별 해야할 일 정리 - 1
update함수
- update 함수에서 dump 데이터 호출되고 결과값은 csvs라는 리스트가 생김
- csvs에들어가는 csv는 카테고리별 apk 정보
- 여기서 csvs 리스트는 차트의 모든 apk 정보들이 담겨있음

즉, csvs에 담겨있는 것이 모든 apk 정보들이니 이를 잘 전처리해서 해주면 appendRow에 전달해주면 됨 (길이만큼)




### 추가로 하면 좋을 것
- 최신 데이터가 위로 가도록
- 이건 시트 자체에서 할 수 있지 않을까?





이 방법은 지금 모든 csvs 파일 정보가 들어오니까 한 라인에 모든 정보가 들어감
```JS
var properties = PropertiesService.getScriptProperties();
// var charts = ['apps_topselling_free', 'apps_topselling_paid', 'apps_topgrossing', 'apps_movers_shakers'];
var charts = ['apps_movers_shakers'];
var categoryIds = ['BUSINESS'];

// var categoryIds = ['DATING', 'ANDROID_WEAR', 'PHOTOGRAPHY', 'AUTO_AND_VEHICLES', 'LIBRARIES_AND_DEMO', 'FINANCE', 'GAME_ADVENTURE', 'EDUCATION', 'TRAVEL_AND_LOCAL', 'BEAUTY', 'SPORTS', 'GAME_STRATEGY', 'GAME_WORD', 'MEDICAL', 'GAME_SIMULATION', 'HOUSE_AND_HOME', 'VIDEO_PLAYERS', 'FOOD_AND_DRINK', 'GAME_CARD', 'GAME_SPORTS', 'GAME_ACTION', 'GAME_RACING', 'GAME_PUZZLE', 'BUSINESS', 'EVENTS', 'GAME_CASUAL', 'WEATHER', 'ENTERTAINMENT', 'NEWS_AND_MAGAZINES', 'GAME_ARCADE', 'SHOPPING', 'COMMUNICATION', 'COMICS', 'HEALTH_AND_FITNESS', 'ART_AND_DESIGN', 'PERSONALIZATION', 'WATCH_FACE', 'SOCIAL', 'MAPS_AND_NAVIGATION', 'TOOLS', 'GAME_CASINO', 'LIFESTYLE', 'GAME_MUSIC', 'GAME_ROLE_PLAYING', 'PARENTING', 'GAME_BOARD', 'GAME_TRIVIA', 'PRODUCTIVITY', 'MUSIC_AND_AUDIO', 'GAME_EDUCATIONAL', 'BOOKS_AND_REFERENCE'];

function synchronize() {
  // if (!isUpdateNeeded()) {
  //   console.log("Alread updated recently");
  //   return;
  // }

  var now = new Date();
  properties.setProperty("UPDATED_AT", now.getTime().toString());
  
  var ss = SpreadsheetApp.getActive();
  var sheets = ss.getSheets();
  for (var i=0; i<sheets.length; i++) {
    update(sheets[i]);
  }
}

function isUpdateNeeded() {
  var milliseconds = properties.getProperty('UPDATED_AT');
  if (milliseconds === undefined) {
    return true;
  }

  var now = new Date();
  var updated = new Date(milliseconds);
  var diffDays = (now - updated) / (1000 * 60 * 60 * 24);
  return diffDays > 1;
} 

function getKstTime() {
  var cur_date = new Date();
  var utc = cur_date.getTime() + (cur_date.getTimezoneOffset() * 60 * 1000);
  var time_diff = 9 * 60 * 60 * 1000;
  var cur_date_korea = new Date(utc + (time_diff));
  var year = cur_date_korea.getFullYear()
  var month = cur_date_korea.getMonth() + 1
  var date = cur_date_korea.getDate()

  if (date < 10 && date > 0) {
    date = '0' + date
  }

  var result = year + '-0' + month + '-' + date
  return result
}

function update(sheet) {
  for (var i=0; i<charts.length; i++) {
    var chart = charts[i];
    if (sheet.getName() == charts[i]) {
      var csvs = Array();
      for (var j=0; j<categoryIds.length; j++) {
        var headerNeeded = j == 0;
        console.log(`CHART : ${chart} - ${categoryIds[j]} PROCESSING`)
        var csv = dump(chart, categoryIds[j], headerNeeded);
        var data = csv.split('\n')
        for (var k = 1; k < 2; k++) {
          // console.log(`push data >>> ${data[k]}`)
          csvs.push(data[k])
        }
      }
      appneRow(sheet, csvs)
      // pasteCSV(sheet, csvs.join(''));
    }
  }
}

function appneRow(sheet, csvs) {
  const newApkArr = Array()
  for (var i = 0; i < csvs.length; i++) {
    var strAPKData = csvs[i]
    // console.log(`strAPKData:${strAPKData}`)
    const splitedAPKDatas = strAPKData.split(/"|"."/)
    // console.log(`splitedAPKDatas: ${splitedAPKDatas}`)
    for (var j = 1; j < splitedAPKDatas.length-1; j++) {
      if (splitedAPKDatas[j] == "," || splitedAPKDatas[j] == " ") {
        continue
      }
      newApkArr.push(splitedAPKDatas[j])
    }
  }
  // console.log("========================================")
  // for (var i = 0; i < newApkArr.length; i++) {
  //   console.log(newApkArr[i])
  // }
  // console.log("========================================")
  console.log(`newApkArr >>> ${newApkArr}`)
  // var rowData = ["hello", "I", "am", "Changhwan"]
  // var lastRow = sheet.getRange("a1").getDataRegion().getLastRow();
  // sheet.getRange(lastRow + 1, 1, 1, 4).setValues([rowData])
  sheet.appendRow(newApkArr)
  
  // 메모
  // newArray를 담고 있는 Array를 하나 만들면 됨 
  // 거기서 newArray를 꺼내면서 추가 로직을 돌림
  // console.log(lastRow)
  // Sheets.Spreadsheets.Values.append(resource,sheetId, "a:v")
}

function pasteCSV(sheet, csv) {
  var ss = SpreadsheetApp.getActive();
  var resource = {
    requests: [
      {
        pasteData: {
          data: csv,
          coordinate: {
            sheetId: sheet.getSheetId()
          },
          delimiter: ',',
        },
      }
    ],
  };
  SpreadsheetApp.flush();
  Sheets.Spreadsheets.batchUpdate(resource, ss.getId());
}

function dump(chart, categoryId, header) {
  var writeDate = getKstTime()
  let url = `https://q0qjuqzaii.execute-api.ap-northeast-2.amazonaws.com/Prod/dump?countryCode=kr&chart=${chart}&categoryId=${categoryId}&writeDate=2022-07-21&header=${header}`;
  var res = UrlFetchApp.fetch(url);
  return res.getContentText();
}
```
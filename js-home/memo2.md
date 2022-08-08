```JS
var properties = PropertiesService.getScriptProperties();
// var charts = ['apps_topselling_free', 'apps_topselling_paid', 'apps_topgrossing', 'apps_movers_shakers'];
var charts = ['apps_movers_shakers'];
var categoryIds = ['BUSINESS', 'GAME_PUZZLE', 'ANDROID_WEAR'];

// var categoryIds = ['DATING', 'ANDROID_WEAR', 'PHOTOGRAPHY', 'AUTO_AND_VEHICLES', 'LIBRARIES_AND_DEMO', 'FINANCE', 'GAME_ADVENTURE', 'EDUCATION', 'TRAVEL_AND_LOCAL', 'BEAUTY', 'SPORTS', 'GAME_STRATEGY', 'GAME_WORD', 'MEDICAL', 'GAME_SIMULATION', 'HOUSE_AND_HOME', 'VIDEO_PLAYERS', 'FOOD_AND_DRINK', 'GAME_CARD', 'GAME_SPORTS', 'GAME_ACTION', 'GAME_RACING', 'GAME_PUZZLE', 'BUSINESS', 'EVENTS', 'GAME_CASUAL', 'WEATHER', 'ENTERTAINMENT', 'NEWS_AND_MAGAZINES', 'GAME_ARCADE', 'SHOPPING', 'COMMUNICATION', 'COMICS', 'HEALTH_AND_FITNESS', 'ART_AND_DESIGN', 'PERSONALIZATION', 'WATCH_FACE', 'SOCIAL', 'MAPS_AND_NAVIGATION', 'TOOLS', 'GAME_CASINO', 'LIFESTYLE', 'GAME_MUSIC', 'GAME_ROLE_PLAYING', 'PARENTING', 'GAME_BOARD', 'GAME_TRIVIA', 'PRODUCTIVITY', 'MUSIC_AND_AUDIO', 'GAME_EDUCATIONAL', 'BOOKS_AND_REFERENCE'];

function synchronize() {
  var now = new Date();
  properties.setProperty("UPDATED_AT", now.getTime().toString());
  
  var ss = SpreadsheetApp.getActive();
  var sheets = ss.getSheets();
  for (var i=0; i<sheets.length; i++) {
    update(sheets[i]);
  }
}

function update(sheet) {
  for (var i=0; i<charts.length; i++) {
    var chart = charts[i];
    if (sheet.getName() == charts[i]) {
      var csvs = Array(); // 전체 한 차트의 모든 apk 데이터들
      for (var j=0; j<categoryIds.length; j++) {
        var headerNeeded = j == 0;
        console.log(`CHART : ${chart} - ${categoryIds[j]} PROCESSING`)
        var csv = dump(chart, categoryIds[j], headerNeeded); // 한 카테고리의 정보가 나옴 150개 정보가 나오고 이걸 50번 반복함
        // csv 데이터는? >> 한 카테고리의 apk 정보들 
        // console.log(`csv >>> ${csv}`)
        csvs.push(csv) 
        // var data = csv.split('\n')
        // for (var k = 1; k < 2; k++) {
        //   csvs.push(data[k])
        // }
      }
      console.log(`csvs size>> ${csvs.length}`) 
      csvs.forEach (csv => {console.log("=========="); console.log(csv)})
      // csvs.forEach (csv => stringProcessor(csv))
      // appneRow(sheet, csvs)
    }
  }
}

function stringProcessor(csv) {
  console.log("Start String Processor")
  var datas = csv.split('\n')
  datas.forEach (
    data => apkProcessor(data)
  )
}

function apkProcessor(strApk) {
  const splitedAPKDatas = strApk.split(/"|"."/)
  const newAPKDatas = Array() // 전처리된 하나의 정보 <= 1차원
  for (var i = 1; i < splitedAPKDatas.length-1; i++) {
    if (splitedAPKDatas[i] == "," || splitedAPKDatas[i] == " ") {
        continue
      }
      newAPKDatas.push(splitedAPKDatas[i])
  }
}


function apkProcessing() {

  return splitedApkDatas
}

function newAppendRow(sheet, data:list[]) {
  sheet.appendRow(data)
} 

function appneRow(sheet, csvs) {
  // csvs는 카테고리별 apk 정보 리스트
  const newApkArr = Array()
  // 전처리와 아래 append를 분리
  for (var i = 0; i < csvs.length; i++) {
    var strAPKData = csvs[i] // 즉 이건 카테고리별 apk를 처리하는 것
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


// function pasteCSV(sheet, csv) {
//   var ss = SpreadsheetApp.getActive();
//   var resource = {
//     requests: [
//       {
//         pasteData: {
//           data: csv,
//           coordinate: {
//             sheetId: sheet.getSheetId()
//           },
//           delimiter: ',',
//         },
//       }
//     ],
//   };
//   SpreadsheetApp.flush();
//   Sheets.Spreadsheets.batchUpdate(resource, ss.getId());
// }

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

function dump(chart, categoryId, header) {
  var writeDate = getKstTime()
  let url = `https://q0qjuqzaii.execute-api.ap-northeast-2.amazonaws.com/Prod/dump?countryCode=kr&chart=${chart}&categoryId=${categoryId}&writeDate=2022-07-21&header=${header}`;
  var res = UrlFetchApp.fetch(url);
  return res.getContentText();
}
```


### 밥 먹고 와서
1. 위에 내용 다시 숙지 후 데이터 전처리 계속
2. 다시 집어보면 문자열 processor에는 하나의 apk 정보 str을 받아서 list[str]로 변환
3. processor에 전달하는 과정만 잘 정리하면 됨
4. update의 결과는 csvs => csvs는 카테고리 리스트 csv는 카테고리 하위의 apk list
5. 따라서 카테고리별로 전처리 띄우고
6. 카테고리별에서 하나의 apk를 스플릿해서 처리한다.

사실 생각해보면
1. csvs에 넘기지말고
2. dump 메서드의 추출결과가 카테고리의 apk 정보들이니 dump의 결과를 차라리 processor에 던져주고
3. processor가 처리하면 될 듯?


```JS
var properties = PropertiesService.getScriptProperties();
// var charts = ['apps_topselling_free', 'apps_topselling_paid', 'apps_topgrossing', 'apps_movers_shakers'];
var charts = ['apps_movers_shakers'];
var categoryIds = ['EDUCATION'];
// var categoryIds = ['DATING', 'ANDROID_WEAR', 'PHOTOGRAPHY', 'AUTO_AND_VEHICLES', 'LIBRARIES_AND_DEMO', 'FINANCE', 'GAME_ADVENTURE', 'EDUCATION', 'TRAVEL_AND_LOCAL', 'BEAUTY', 'SPORTS', 'GAME_STRATEGY', 'GAME_WORD', 'MEDICAL', 'GAME_SIMULATION', 'HOUSE_AND_HOME', 'VIDEO_PLAYERS', 'FOOD_AND_DRINK', 'GAME_CARD', 'GAME_SPORTS', 'GAME_ACTION', 'GAME_RACING', 'GAME_PUZZLE', 'BUSINESS', 'EVENTS', 'GAME_CASUAL', 'WEATHER', 'ENTERTAINMENT', 'NEWS_AND_MAGAZINES', 'GAME_ARCADE', 'SHOPPING', 'COMMUNICATION', 'COMICS', 'HEALTH_AND_FITNESS', 'ART_AND_DESIGN', 'PERSONALIZATION', 'WATCH_FACE', 'SOCIAL', 'MAPS_AND_NAVIGATION', 'TOOLS', 'GAME_CASINO', 'LIFESTYLE', 'GAME_MUSIC', 'GAME_ROLE_PLAYING', 'PARENTING', 'GAME_BOARD', 'GAME_TRIVIA', 'PRODUCTIVITY', 'MUSIC_AND_AUDIO', 'GAME_EDUCATIONAL', 'BOOKS_AND_REFERENCE'];

function synchronize() {
  var now = new Date();
  properties.setProperty("UPDATED_AT", now.getTime().toString());
  
  var ss = SpreadsheetApp.getActive();
  var sheets = ss.getSheets();
  for (var i=0; i<sheets.length; i++) {
    originUpdate(sheets[i]);
  }
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

function originUpdate (sheet) {
  for (var i=0; i<charts.length; i++) {
    var chart = charts[i];
    if (sheet.getName() == charts[i]) {
      var chartAPKs = Array();
      for (var j=0; j<categoryIds.length; j++) {
        var headerNeeded = j == 0;
        console.log(`CHART : ${chart} - ${categoryIds[j]} PROCESSING`)
        var categoryAPKs = dump(chart, categoryIds[j], headerNeeded);
        chartAPKs.push(categoryAPKs)
      }
      chartAPKProcessor(sheet, chartAPKs.join())
    }
  }
}

function chartAPKProcessor(sheet, chartAPKs) {
  console.log("Start chart apk processor")
  var rowDatas = Array()
  var splitedAPKInfo = chartAPKs.split('\n')
  for (var i = 1; i < splitedAPKInfo.length - 1; i++) {
    rowDatas.push(convetToRowData(splitedAPKInfo[i]))
  }

  if (rowDatas.length > 0) {
    rowDatas.forEach(
      data => {
        appendRow(sheet, data)
      }
    )
  } else {
    console.log("Data is Not Exist")
  }
}

function convetToRowData(strAPKData) {
  const splitedAPKData = strAPKData.split(/"|"."/)
  var rowData = Array()
  for (var i = 1; i < splitedAPKData.length - 1; i++) {
      if (splitedAPKData[i] == "," || splitedAPKData[i] == " ") {
        continue
      }
      rowData.push(splitedAPKData[i])
    }
  return rowData
}

function appendRow(sheet, data) {
  // sheet.appendRow(data)
  // 시험
  var rowData = ['hello', 'i', 'am', 'changhwan']
  var rowData2 = ['hello', 'you', 'are', 'kewqoew']
  var rowData3 = ['hello', 'they', 'are', 'ewqeqwe']
  var lastRow = sheet.getRange("a1").getDataRegion().getLastRow();
  sheet.getRange(lastRow + 1, 1, 3, 4).setValues([rowData, rowData2, rowData3])
}

function dump(chart, categoryId, header) {
  var writeDate = getKstTime()
  let url = `https://q0qjuqzaii.execute-api.ap-northeast-2.amazonaws.com/Prod/dump?countryCode=kr&chart=${chart}&categoryId=${categoryId}&writeDate=2022-07-21&header=${header}`;
  var res = UrlFetchApp.fetch(url);
  return res.getContentText();
}
```

### 잘 되는 것
```JS
var properties = PropertiesService.getScriptProperties();
// var charts = ['apps_topselling_free', 'apps_topselling_paid', 'apps_topgrossing', 'apps_movers_shakers'];
var charts = ['apps_movers_shakers'];
// var categoryIds = ['EDUCATION'];
// var categoryIds = ['DATING', 'ANDROID_WEAR', 'PHOTOGRAPHY', 'AUTO_AND_VEHICLES', 'LIBRARIES_AND_DEMO', 'FINANCE', 'GAME_ADVENTURE', 'EDUCATION', 'TRAVEL_AND_LOCAL', 'BEAUTY', 'SPORTS', 'GAME_STRATEGY', 'GAME_WORD', 'MEDICAL', 'GAME_SIMULATION', 'HOUSE_AND_HOME', 'VIDEO_PLAYERS', 'FOOD_AND_DRINK', 'GAME_CARD', 'GAME_SPORTS', 'GAME_ACTION', 'GAME_RACING', 'GAME_PUZZLE', 'BUSINESS', 'EVENTS', 'GAME_CASUAL', 'WEATHER', 'ENTERTAINMENT', 'NEWS_AND_MAGAZINES', 'GAME_ARCADE', 'SHOPPING', 'COMMUNICATION', 'COMICS', 'HEALTH_AND_FITNESS', 'ART_AND_DESIGN', 'PERSONALIZATION', 'WATCH_FACE', 'SOCIAL', 'MAPS_AND_NAVIGATION', 'TOOLS', 'GAME_CASINO', 'LIFESTYLE', 'GAME_MUSIC', 'GAME_ROLE_PLAYING', 'PARENTING', 'GAME_BOARD', 'GAME_TRIVIA', 'PRODUCTIVITY', 'MUSIC_AND_AUDIO', 'GAME_EDUCATIONAL', 'BOOKS_AND_REFERENCE'];

var categoryIds = ["GAME_TRIVIA", "SOCIAL", "GAME_CASUAL", "WEATHER", "PARENTING", "ART_AND_DESIGN", "GAME_ADVENTURE", "LIFESTYLE", "ENTERTAINMENT", "GAME_ARCADE", "GAME_PUZZLE", "GAME_SPORTS", "NEWS_AND_MAGAZINES", "BUSINESS", "COMICS", "GAME_CARD", "HEALTH_AND_FITNESS", "MAPS_AND_NAVIGATION", "MUSIC_AND_AUDIO", "MEDICAL", "COMMUNICATION", "GAME_SIMULATION", "GAME_CASINO", "TOOLS", "SPORTS", "DATING", "GAME_MUSIC", "BOOKS_AND_REFERENCE", "PERSONALIZATION", "GAME_EDUCATIONAL", "PHOTOGRAPHY", "LIBRARIES_AND_DEMO", "GAME_ACTION", "AUTO_AND_VEHICLES", "GAME_BOARD", "FOOD_AND_DRINK", "FINANCE", "GAME_STRATEGY", "EVENTS", "GAME_ROLE_PLAYING", "ANDROID_WEAR", "TRAVEL_AND_LOCAL", "WATCH_FACE", "GAME_RACING", "VIDEO_PLAYERS", "PRODUCTIVITY", "EDUCATION", "SHOPPING", "HOUSE_AND_HOME", "BEAUTY", "GAME_WORD"]

function synchronize() {
  var now = new Date();
  properties.setProperty("UPDATED_AT", now.getTime().toString());
  
  var ss = SpreadsheetApp.getActive();
  var sheets = ss.getSheets();
  for (var i=0; i<sheets.length; i++) {
    originUpdate(sheets[i]);
  }
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

function originUpdate (sheet) {
  for (var i=0; i<charts.length; i++) {
    var chart = charts[i];
    if (sheet.getName() == charts[i]) {
      var chartAPKs = Array();
      for (var j=0; j<categoryIds.length; j++) {
        var headerNeeded = j == 0;
        console.log(`CHART : ${chart} - ${categoryIds[j]} PROCESSING`)
        var categoryAPKs = dump(chart, categoryIds[j], headerNeeded);
        chartAPKs.push(categoryAPKs)
      }
      chartAPKProcessor(sheet, chartAPKs.join())
    }
  }
}

function chartAPKProcessor(sheet, chartAPKs) {
  console.log("Start chart apk processor")
  var rowDatas = Array()
  var splitedAPKInfo = chartAPKs.split('\n')
  for (var i = 1; i < splitedAPKInfo.length - 1; i++) {
    rowDatas.push(convetToRowData(splitedAPKInfo[i]))
  }

  if (rowDatas.length > 0) {
    appendRow(sheet, rowDatas)
  } else {
    console.log("Data is Not Exist")
  }
}

function convetToRowData(strAPKData) {
  const splitedAPKData = strAPKData.split(/"|"."/)
  var rowData = Array()
  for (var i = 1; i < splitedAPKData.length - 1; i++) {
      if (splitedAPKData[i] == "," || splitedAPKData[i] == " ") {
        continue
      }
      rowData.push(splitedAPKData[i])
    }
  return rowData
}

function appendRow(sheet, rowDatas) {
  console.log("start append row data")
  var lastRow = sheet.getRange("a1").getDataRegion().getLastRow();
  console.log(`rowDatas.length >>>> ${rowDatas.length}`)
  for (var i = 0; i < rowDatas.length; i++) {
    sheet.getRange((lastRow + i + 1), 1, 1, rowDatas[i].length).setValues([rowDatas[i]])  
  }
}

function dump(chart, categoryId, header) {
  var writeDate = getKstTime()
  let url = `https://q0qjuqzaii.execute-api.ap-northeast-2.amazonaws.com/Prod/dump?countryCode=kr&chart=${chart}&categoryId=${categoryId}&writeDate=2022-07-21&header=${header}`;
  var res = UrlFetchApp.fetch(url);
  return res.getContentText();
}
```


```
packageName,displayName,shortDescription,downloads,developerName,developerWebsite,developerEmail,developerAddress,iconUrl,categoryId,categoryName,updatedOn,versionCode,versionName,permissions,targetSdk,isFree,price,rating,size,sdks,writeDate
"com.zamface","잼페이스 : 퍼스널컬러 인생템 추천","Personal color free diagnosis and beauty video review to find life items","1000000.0","ZAMFACE","http://www.zamface.co.kr","admin@zamface.co.kr","","https://play-lh.googleusercontent.com/B8YLX4W-GvLvypvTWPJPoksN0fKtpzq16s0Lp_cTLdyorRu85jefs1_MMVNH9DX-sOo","3.0","Beauty","Jul 20, 2022","202201.0","2.22.1","android.permission.ACCESS_NETWORK_STATE,android.permission.ACCESS_WIFI_STATE,android.permission.CAMERA,android.permission.FOREGROUND_SERVICE,android.permission.INTERNET,android.permission.READ_APP_BADGE,android.permission.READ_CONTACTS,android.permission.READ_EXTERNAL_STORAGE,android.permission.READ_PHONE_STATE,android.permission.READ_PROFILE,android.permission.RECEIVE_BOOT_COMPLETED,android.permission.RECORD_AUDIO,android.permission.SYSTEM_ALERT_WINDOW,android.permission.VIBRATE,android.permission.WAKE_LOCK,android.permission.WRITE_EXTERNAL_STORAGE,com.anddoes.launcher.permission.UPDATE_COUNT,com.google.android.c2dm.permission.RECEIVE,com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE,com.google.android.gms.permission.AD_ID,com.htc.launcher.permission.READ_SETTINGS,com.htc.launcher.permission.UPDATE_SHORTCUT,com.huawei.android.launcher.permission.CHANGE_BADGE,com.huawei.android.launcher.permission.READ_SETTINGS,com.huawei.android.launcher.permission.WRITE_SETTINGS,com.majeur.launcher.permission.UPDATE_BADGE,com.oppo.launcher.permission.READ_SETTINGS,com.oppo.launcher.permission.WRITE_SETTINGS,com.sec.android.provider.badge.permission.READ,com.sec.android.provider.badge.permission.WRITE,com.sonyericsson.home.permission.BROADCAST_BADGE,com.sonymobile.home.permission.PROVIDER_INSERT_BADGE,me.everything.badger.permission.BADGE_COUNT_READ,me.everything.badger.permission.BADGE_COUNT_WRITE","30.0","true","","4.184492","1.07160024E8","protobuf,dagger,lottie,fresco,facebook,kakao_api,kotlin,zxing,google_cloud_messaging,react_native,kotlin_coroutines,airbridge,amplitude,firebase_analytics,retrofit,okio,okhttp,admob,gson,glide","2022-07-24"
"com.kakao.beauty.hairshop","카카오헤어샵","Booking is easier, style is richer! From hair salon to nail shop reservation!","1000000.0","Kakao Corp.","https://hairshop.kakao.com","help.notice@kakaocorp.com","제주특별자치도 제주시 첨단로 242 (주)카카오","https://play-lh.googleusercontent.com/_9oS66rnjih-0-xUXq2-UJu8F2YUGL7quSSviCPj5RhfnuAQ_t9x6wQ5J_AFu7_bJ8jV","3.0","Beauty","May 30, 2022","2.20527001E8","4.7.5","android.permission.ACCESS_COARSE_LOCATION,android.permission.ACCESS_FINE_LOCATION,android.permission.ACCESS_NETWORK_STATE,android.permission.ACCESS_WIFI_STATE,android.permission.CAMERA,android.permission.DIAL_PHONE,android.permission.INTERNET,android.permission.READ_EXTERNAL_STORAGE,android.permission.REORDER_TASKS,android.permission.WAKE_LOCK,android.permission.WRITE_EXTERNAL_STORAGE,com.google.android.c2dm.permission.RECEIVE,com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE,com.google.android.gms.permission.AD_ID","31.0","true","","4.352022","3.1308502E7","protobuf,lottie,facebook,kakao_api,kotlin,dagger_hilt,google_cloud_messaging,firebase_analytics,retrofit,okio,appsflyer,stetho,okhttp,gson,glide,picasso","2022-07-24"
"kr.co.company.hwahae","Hwahae - analyzing cosmetics","For people who want to check the ingredients of cosmetics. Join 'Hwahae' now!","5000000.0","BirdView","http://www.hwahae.co.kr/","cs@hwahae.co.kr","","https://play-lh.googleusercontent.com/5vrrZzL4jKg4Rs_SdGL9MuQbmxI1EmpQW9fuDMzY7N5-UuvMtJ1a4Kten6exClZSMfBH","3.0","Beauty","Jul 20, 2022","326.0","7.7.1","android.permission.ACCESS_NETWORK_STATE,android.permission.ACCESS_WIFI_STATE,android.permission.INTERNET,android.permission.READ_EXTERNAL_STORAGE,android.permission.REORDER_TASKS,android.permission.VIBRATE,android.permission.WAKE_LOCK,android.permission.WRITE_EXTERNAL_STORAGE,com.google.android.c2dm.permission.RECEIVE,com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE,com.google.android.providers.gsf.permission.READ_GSERVICES","30.0","true","","4.100904","2.0157605E7","protobuf,lottie,braze,facebook,kakao_api,zxing,google_cloud_messaging,firebase_analytics,retrofit,appsflyer,okhttp,admob,gson,glide,rxjava","2022-07-24"
"com.gangnam.sister","GangnamUnni - Medical beauty","GangnamUnni, the medical beauty app with reviews, discounts, and clinic rsvp","1000000.0","강남언니","https://www.gangnamsister.com","cs@healingpaper.com","서울특별시 강남구 테헤란로 124, 삼원타워 13층 (힐링페이퍼)","https://play-lh.googleusercontent.com/ZQUodHtGHoPbadeChBVYuwc4KWiAyjYonDoCR-3jE4xqd_HJHNfsyHVPmNboBfF7eRg","3.0","Beauty","Jul 19, 2022","413.0","3.120.1","android.permission.ACCESS_NETWORK_STATE,android.permission.ACCESS_WIFI_STATE,android.permission.CALL_PHONE,android.permission.CAMERA,android.permission.CHANGE_WIFI_STATE,android.permission.FOREGROUND_SERVICE,android.permission.INTERNET,android.permission.READ_EXTERNAL_STORAGE,android.permission.READ_PHONE_STATE,android.permission.RECEIVE_BOOT_COMPLETED,android.permission.VIBRATE,android.permission.WAKE_LOCK,android.permission.WRITE_EXTERNAL_STORAGE,com.google.android.c2dm.permission.RECEIVE,com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE,com.google.android.gms.permission.ACTIVITY_RECOGNITION,com.google.android.gms.permission.AD_ID,com.google.android.providers.gsf.permission.READ_GSERVICES","30.0","true","","4.551579","1.10804319E8","protobuf,lottie,kakao_ad,slf4j,braze,facebook,kakao_api,kotlin,dagger_hilt,google_cloud_messaging,amplitude,joda,firebase_analytics,retrofit,appsflyer,google_analytics,okhttp,gson,glide,guava,rxjava","2022-07-24"
"com.rimankorea.myoffice","리만코리아 My Office","It is a dedicated application for salespersons, dealers (including branches and headquarters) provided by Riman Korea.","50000.0","주식회사 리만","https://www.rimankorea.com","it@rimankorea.co.kr","","https://play-lh.googleusercontent.com/WPbjF-GnkKMmaxx8yrPA2L15XdJZbe1JF268UhRzr3CZBOdxQGRPhjqATNK6ZB4YIFQ","3.0","Beauty","May 17, 2022","8.0","1.0.8","android.permission.ACCESS_DOWNLOAD_MANAGER,android.permission.ACCESS_NETWORK_STATE,android.permission.ACCESS_WIFI_STATE,android.permission.CAMERA,android.permission.INTERNET,android.permission.READ_EXTERNAL_STORAGE,android.permission.WRITE_EXTERNAL_STORAGE","31.0","true","","4.4126983","3401332.0","kotlin,guava","2022-07-24"
"godticket.mobile","여신티켓 - 피부, 쁘띠, 성형, 다이어트 가격비교","Credit Ticket is a service that allows you to compare various skin and plastic surgery events and pay in advance. Take care of your skin with a credit ticket.","500000.0","Fastlane Inc.","https://yeoshin.co.kr","contact@fastlane.kr","서울시 강남구 테헤란로 423, 현대타워 801호","https://play-lh.googleusercontent.com/WfqH8izmWBTClntS9uN8cSne9waLNQJFDJYSC_F0earMbYS6VgxqBwdCusJf0WFvjw","3.0","Beauty","Jul 17, 2022","99.0","2.1.13","android.permission.ACCESS_COARSE_LOCATION,android.permission.ACCESS_FINE_LOCATION,android.permission.ACCESS_NETWORK_STATE,android.permission.ACCESS_WIFI_STATE,android.permission.CAMERA,android.permission.FOREGROUND_SERVICE,android.permission.INTERNET,android.permission.READ_EXTERNAL_STORAGE,android.permission.VIBRATE,android.permission.WAKE_LOCK,android.permission.WRITE_EXTERNAL_STORAGE,com.google.android.c2dm.permission.RECEIVE,com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE,com.google.android.gms.permission.AD_ID","30.0","true","","4.2827225","1.3778143E7","lottie,kakao_ad,facebook,kakao_api,kotlin,dagger_hilt,google_cloud_messaging,naver_api,firebase_analytics,retrofit,appsflyer,okhttp,gson,glide,rxjava,picasso","2022-07-24"
"com.sleet.beautyplastic","바비톡 - 1등 성형/시술 정보앱","From plastic surgery and skin treatment to side effects, meticulously bobbitok","1000000.0","BABITALK","http://babitalk.com/","cs@babitalk.com","","https://play-lh.googleusercontent.com/Kd-CSSEGkYP6ULkmX973Kdk82oS81wZR5HiffXVcM__YmUczcemQVjlMj1GxsUEcAeo","3.0","Beauty","Jul 15, 2022","360.0","5.38.0","android.permission.ACCESS_NETWORK_STATE,a
```
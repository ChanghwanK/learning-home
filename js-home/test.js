var properties = PropertiesService.getScriptProperties();
// var charts = ['apps_topselling_free', 'apps_topgrossing', 'apps_movers_shakers'];
var charts = ['apps_topselling_free'];
// var categoryIds = ['EDUCATION'];
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
  var lastRow = sheet.getRange("a1").getDataRegion().getLastRow();
  var splitedAPKInfo = chartAPKs.split('\n')
  for (var i = 1; i < splitedAPKInfo.length - 1; i++) {
    rowDatas.push(convetToRowData(splitedAPKInfo[i]))
  }

  if (rowDatas.length > 0) {
    appendRow(sheet, rowDatas, lastRow)
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

function appendRow(sheet, rowDatas, lastRow) {
  console.log("start append row data")
  // 여기서 실행시간 줄여볼 수 있을 것 같음
  // setValues에 3000개 다 넣어보기
  // sheet.getRange(lastRow+1, 1, rowDatas.length, 22).setValues(rowDatas)
  for (var i = 0; i < rowDatas.length; i++) {
    sheet.getRange((lastRow + i + 1), 1, 1, rowDatas[i].length).setValues([rowDatas[i]])  
  }
  console.log("End append row data")  
}

function dump(chart, categoryId, header) {
  var writeDate = getKstTime()
  let url = `https://q0qjuqzaii.execute-api.ap-northeast-2.amazonaws.com/Prod/dump?countryCode=kr&chart=${chart}&categoryId=${categoryId}&writeDate=2022-07-24&header=${header}`;
  var res = UrlFetchApp.fetch(url);
  return res.getContentText();
}
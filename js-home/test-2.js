var titleValues = ["The Big New Movie 2012", "The Big New Movie"];
var titleObject = {};
var index = 0;
titleValues.forEach(function(value) {
    index++;
    var titleKey = ":titlevalue"+index;
    titleObject[titleKey.toString()] = value;
});

var params = {
    TableName : "Movies",
    FilterExpression : "title IN ("+Object.keys(titleObject).toString()+ ")",
    ExpressionAttributeValues : titleObject
};

console.log(params)
function weeks() {
    var weeks	= new Array('日','月','火','水','木','金','土');
    var today	= new Date();
    var week	= weeks[today.getDay()];
    var string	= '';
    switch(week) {
    case '日':
	string = 'Sunday';
	break;
    case '月':
	string = 'Monday';
	break;
    case '火':
	string = 'Tuesday';
	break;
    case '水':
	string = 'Wednesday';
	break;
    case '木':
	string = 'Thursday';
	break;
    case '金':
	string = 'Friday';
	break;
    case '土':
	string = 'Saturday';
	break;
    default:
	string = '';
	break;
    }
    document.write( string );
}
function course() {
    var today	= new Date();
    var getday	= today.getDay();
    return getday;
}

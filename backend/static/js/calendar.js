document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        selectable: true,
        editable: true,
        events: [],
        select: function (info) {
            let title = prompt('Enter shift details:');
            if (title) {
                calendar.addEvent({
                    title: title,
                    start: info.startStr,
                    end: info.endStr,
                    allDay: info.allDay
                });
                alert('Shift added.');
            }
        },
        eventClick: function (info) {
            if (confirm('Do you want to delete this shift?')) {
                info.event.remove();
                alert('Shift deleted.');
            }
        }
    });
    calendar.render();
});

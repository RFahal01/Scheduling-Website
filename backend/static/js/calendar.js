document.addEventListener('DOMContentLoaded', function () {
    // Get the calendar element from the DOM
    var calendarEl = document.getElementById('calendar');

    // Initialize the FullCalendar instance
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth', // Set the initial view to month view
        selectable: true, // Allow date selection
        editable: true, // Allow event editing
        events: [], // Initialize with no events

        // Function to handle date selection
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

        // Function to handle event click
        eventClick: function (info) {
            if (confirm('Do you want to delete this shift?')) {
                info.event.remove();
                alert('Shift deleted.');
            }
        }
    });

    // Render the calendar
    calendar.render();
});
document.addEventListener('DOMContentLoaded', function () {
    // Get the calendar element by its ID
    var calendarEl = document.getElementById('calendar');

    // Initialize the FullCalendar instance
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth', // Set the initial view to month grid
        selectable: true, // Allow date selection
        editable: true, // Allow event editing
        events: [], // Initialize with an empty events array

        // Function to handle date selection
        select: function (info) {
            // Prompt the user to enter shift details
            let title = prompt('Enter shift details:');
            if (title) {
                // Add the new event to the calendar
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
            // Confirm if the user wants to delete the event
            if (confirm('Do you want to delete this shift?')) {
                // Remove the event from the calendar
                info.event.remove();
                alert('Shift deleted.');
            }
        }
    });

    // Render the calendar
    calendar.render();
});
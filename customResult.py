from robot.api.deco import keyword

import customResult

data=[]
testcount=0






content1 ="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Table</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        .status-pass {
            color: green;
        }
        .status-fail {
            color: red;
        }
        .summary {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>

<h1>Test Results</h1>

<table id="testTable">
    <thead>
        <tr>
            <th>Serial No.</th>
            <th>Test Name</th>
            <th>Agreement No.</th>
            <th>Status</th>
            <th>Message</th>
        </tr>
    </thead>
    <tbody>
"""

content2="""</tbody>
</table>

<div class="summary" id="summary">
    Total Passed: <span id="totalPassed">0</span><br>
    Total Failed: <span id="totalFailed">0</span>
</div>

<script>
    function updateSummary() {
        const rows = document.querySelectorAll('#testTable tbody tr');
        let passedCount = 0;
        let failedCount = 0;

        rows.forEach(row => {
            const statusCell = row.cells[3]; // Status is the 4th cell (index 3)
            if (statusCell.classList.contains('status-pass')) {
                passedCount++;
            } else if (statusCell.classList.contains('status-fail')) {
                failedCount++;
            }
        });

        document.getElementById('totalPassed').innerText = passedCount;
        document.getElementById('totalFailed').innerText = failedCount;
    }

    // Call the function to update the summary on page load
    updateSummary();
</script>

</body>
</html>
"""
@keyword
def aggFunction(testname, AGNumber, status, message):
    customResult.testcount+=1
    testdata = f"""<tr>
            <td>{customResult.testcount}</td>
            <td>{testname}</td>
            <td>{AGNumber}</td>
            <td class="status-{str.lower(status)}">{status}</td>
            <td>{message}</td>
        </tr>"""
    print(testdata)
    data.append(testdata)
    print(data)


print("Hello world")

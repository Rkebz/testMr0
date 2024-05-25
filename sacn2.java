const http = require('http');

function check_vulnerabilities() {
    try {
        const url = prompt('Enter the website URL (e.g., http://example.com): ');
        http.get(url, (response) => {
            let data = '';
            response.on('data', (chunk) => {
                data += chunk;
            });
            response.on('end', () => {
                const vulnerabilities = data;
                // Perform your vulnerability checks
            });
        }).on('error', (error) => {
            console.error('Error fetching vulnerabilities:', error);
        });
    } catch (error) {
        console.error('Error fetching vulnerabilities:', error);
    }
}

check_vulnerabilities();
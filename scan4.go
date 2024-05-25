package main

import (
    "fmt"
    "net/http"
    "io/ioutil"
    "strings"
)

func checkVulnerabilities() {
    url := prompt("Enter the website URL (e.g., http://example.com): ")
    response, err := http.Get(url)
    if err != nil {
        fmt.Println("Error fetching vulnerabilities:", err)
        return
    }
    defer response.Body.Close()

    if response.StatusCode == http.StatusOK {
        body, err := ioutil.ReadAll(response.Body)
        if err != nil {
            fmt.Println("Error reading response body:", err)
            return
        }

        vulnerabilities := strings.Split(string(body), "\n")
        for _, vulnerability := range vulnerabilities {
            // Perform your vulnerability checks
        }
    } else {
        fmt.Println("Error fetching vulnerabilities: Status code", response.StatusCode)
    }
}

func main() {
    checkVulnerabilities()
}
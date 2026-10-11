package tests;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class GoogleSearchTest {

    WebDriver driver;

    @BeforeEach
    void setUp() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
    }

    @Test
    void testGoogleSearchTitle() {
        driver.get("https://www.google.com");

        String title = driver.getTitle();
        assertTrue(title.contains("Google"), "Заголовок должен содержать слово Google");

        System.out.println("Тест прошёл успешно! Заголовок страницы: " + title);
    }

    @AfterEach
    void tearDown() {
        driver.quit();
    }
}
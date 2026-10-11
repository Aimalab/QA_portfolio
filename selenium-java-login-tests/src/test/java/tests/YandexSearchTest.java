package tests;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class YandexSearchTest {

    WebDriver driver;

    @BeforeEach
    void setUp() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
    }

    @Test
    void testYandexUrl() {
        driver.get("https://www.yandex.ru");

        String currentUrl = driver.getCurrentUrl();
        System.out.println("РЕАЛЬНЫЙ URL СТРАНИЦЫ: [" + currentUrl + "]");

        assertTrue(
                currentUrl.contains("yandex") || currentUrl.contains("dzen"),
                "URL должен содержать yandex или dzen (из-за редиректа Яндекса)"
        );
    }
    @AfterEach
    void tearDown() {
        driver.quit();
    }
}
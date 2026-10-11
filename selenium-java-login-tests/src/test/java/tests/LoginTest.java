package tests;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class LoginTest {

    WebDriver driver;
    WebDriverWait wait;

    @BeforeEach
    void setUp() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        // Создаём объект ожидания с максимальным временем 10 секунд
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    @Test
    void testSuccessfulLogin() {
        driver.get("https://the-internet.herokuapp.com/login");

        driver.findElement(By.id("username")).sendKeys("tomsmith");
        driver.findElement(By.id("password")).sendKeys("SuperSecretPassword!");
        driver.findElement(By.cssSelector("button[type='submit']")).click();

        // Вместо обычного findElement — ждём, пока элемент #flash появится в DOM
        WebElement flashMessage = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.id("flash"))
        );
        String messageText = flashMessage.getText();

        System.out.println("Сообщение после логина: " + messageText);

        assertTrue(messageText.contains("You logged into a secure area"),
                "Ожидалось сообщение об успешном входе");
    }

    @Test
    void testFailedLoginWithWrongPassword() {
        driver.get("https://the-internet.herokuapp.com/login");

        driver.findElement(By.id("username")).sendKeys("tomsmith");
        driver.findElement(By.id("password")).sendKeys("wrongpassword");
        driver.findElement(By.cssSelector("button[type='submit']")).click();

        WebElement flashMessage = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.id("flash"))
        );
        String messageText = flashMessage.getText();

        System.out.println("Сообщение об ошибке: " + messageText);

        assertTrue(messageText.contains("Your password is invalid"),
                "Ожидалось сообщение об ошибке пароля");
    }

    @AfterEach
    void tearDown() {
        driver.quit();
    }
}
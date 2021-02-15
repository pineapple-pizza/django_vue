require("dotenv").config();

const { Builder, By, Key, until } = require("selenium-webdriver");
(async function example() {
  let driver = await new Builder().forBrowser("chrome").build();

  await driver.get(process.env.VUE_APP_URL);
  await driver.findElement(By.name("login")).click();
  await driver
    .findElement(By.name("email"))
    .sendKeys(process.env.VUE_APP_VERIFIED_EMAIL, Key.RETURN);
  await driver
    .findElement(By.name("password"))
    .sendKeys(process.env.VUE_APP_VERIFIED_PASSWORD, Key.RETURN);
  await driver
    .findElement(By.name("submit"))
    .click()
    .then(function() {
      // driver.findElement(By.name("profile_account")).click().then(function() {
      driver.getTitle().then(function(title) {
        setTimeout(function() {
          driver
            .findElement(By.name("search_bar"))
            .sendKeys("salsa", Key.RETURN);
          driver.findElement(By.name("search_submit")).click();
          console.log(title);
          // driver.quit();
        }, 5000);
      });
      // });
    })
    .catch(function(err) {
      console.log("test failed with reason " + err);
      next(err);
      // driver.quit();
    });
})();

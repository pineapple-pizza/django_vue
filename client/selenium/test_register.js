require('dotenv').config();

const { Builder, By, Key, until } = require("selenium-webdriver");
(async function example() {
  let driver = await new Builder().forBrowser("chrome").build();

  await driver.get(process.env.VUE_APP_URL);
  await driver.findElement(By.name("signin")).click();
  await driver
    .findElement(By.name("email_signin"))
    .sendKeys(process.env.VUE_APP_NEW_EMAIL, Key.RETURN);
  await driver
    .findElement(By.name("username_signin"))
    .sendKeys(process.env.VUE_APP_NEW_USERNAME, Key.RETURN);
  await driver
    .findElement(By.name("password_signin"))
    .sendKeys(process.env.VUE_APP_NEW_PASSWORD, Key.RETURN);
  await driver.findElement(By.name("submit")).click();
  // .then(function() {
  //   driver.getTitle().then(function(title) {
  //     setTimeout(function() {
  //       driver.findElement(By.name("favorites")).click();
  //       console.log(title);
  //       // driver.quit();
  //     }, 1000);
  //   });
  // })
  // .catch(function(err) {
  //   console.log("test failed with reason " + err);
  //   // driver.quit();
  // });
})();

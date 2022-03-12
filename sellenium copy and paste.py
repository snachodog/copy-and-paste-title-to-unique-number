// or any locator strategy that you find suitable
        WebElement locOfOrder = driver.findElement(By.id("tainacan-item-metadatum_id-5135"));
Actions act = new Actions(driver);
act.moveToElement(locOfOrder).doubleClick().build().perform();
// catch here is double click on the text will by default select the text
// now apply copy command

driver.findElement(By.id("")).sendKeys(Keys.chord(Keys.CONTROL,"c"));
// now apply the command to paste
driver.findElement (By.xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div/section/div[2]/form/div/div[1]/div[2]/section/div[1]/div[3]/div/div/input")).sendKeys(Keys.chord(Keys.CONTROL, "v"));

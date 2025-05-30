import { test, expect } from '@playwright/test';

test('Doğru istifadəçi adı və şifrə ilə uğurlu giriş', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('[data-test="username"]', 'standard_user');
  await page.fill('[data-test="password"]', 'secret_sauce');
  await page.click('[data-test="login-button"]');
  await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');
});

test('Yanlış istifadəçi adı və şifrə ilə giriş uğursuz olmalıdır', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('[data-test="username"]', 'wrong_user');
  await page.fill('[data-test="password"]', 'wrong_pass');
  await page.click('[data-test="login-button"]');
  await expect(page.locator('[data-test="error"]')).toBeVisible();
  await expect(page.locator('[data-test="error"]')).toContainText('Username and password do not match');
});


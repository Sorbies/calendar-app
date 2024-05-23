const { test, expect } = require('@playwright/test');
const baseURL = "localhost:3000";


test('login error page has an alert', async ( { page } ) => {
    await page.goto(`${baseURL}/signout`);
    await expect(page.getByText('You are not logged in.')).toBeDefined();
})

test('signout page has an alert', async ({ page }) => {
    await page.goto(`${baseURL}/signout`);
    await expect(page.getByText('You have been signed out.')).toBeDefined();
})

test('welcome page doesnt start with an alert', async ({ page }) => {
    await page.goto(`${baseURL}/welcome`);
    await expect(page.getByRole('status', {name: 'authAlert'})).not.toBeAttached(); //asserts that this element doesn't exist
})

test('redirects back to sign in if unauthorized', async ({ page }) => {
    await page.goto(`${baseURL}/calendar`);
    await expect(page).toHaveURL(/login-error/);
});

test('login redirects to home', async ({ page }) => {
    //register an account (may already exist)
    await page.goto(`${baseURL}/welcome`);
    await page.getByRole('textbox', {name: 'username'}).fill('a');
    await page.getByRole('textbox', {name: 'password'}).fill('a');
    await page.getByText('Submit').click();

    //log into that account
    await page.goto(`${baseURL}/welcome`);
    await page.getByText('Already have an account? Log in').click();
    await page.getByRole('textbox', {name: 'username'}).fill('a');
    await page.getByRole('textbox', {name: 'password'}).fill('a');    
    await page.getByText('Submit').click();
    await expect(page).toHaveURL(/home/);
})

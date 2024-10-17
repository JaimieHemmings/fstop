describe('Test Navigation', () => {
  beforeEach(() => {
    cy.setCookie('cookie-consent', 'accepted')
    cy.visit('/')
  })
  it('passes', () => {
    cy.on("uncaught:exception", (e) => {
      console.log("error", e);
      return false;
      });
    //Test navigation links
    cy.visit('/')
    cy.url().should('include', '/')
    cy.visit('/about')
    cy.url().should('include', '/about')
    cy.visit('/portfolio')
    cy.url().should('include', '/portfolio')
    cy.visit('/news')
    cy.url().should('include', '/news')
    cy.visit('/contact')
    cy.url().should('include', '/contact')

    // Test services links
    cy.getDataCy('main-nav').within(() => {
      cy.getDataCy('dropdown-menu-services').click()
      cy.getDataCy('lifestyle').click()
    })

    cy.getDataCy('main-nav').within(() => {
      cy.getDataCy('dropdown-menu-services').click()
      cy.getDataCy('event').click()
    })

    cy.getDataCy('main-nav').within(() => {
      cy.getDataCy('dropdown-menu-services').click()
      cy.getDataCy('property').click()
    })

    cy.getDataCy('main-nav').within(() => {
      cy.getDataCy('dropdown-menu-services').click()
      cy.getDataCy('aerial').click()
    })


    // Test login link
    cy.getDataCy('main-nav').within(() => {
      cy.getDataCy('dropdown-menu-profile').click()
      cy.getDataCy('login-link').click()
    })

    // Test Register link
    cy.getDataCy('main-nav').within(() => {
      cy.getDataCy('dropdown-menu-profile').click()
      cy.getDataCy('register-link').click()
    })

    // Test 404 works
    cy.request({url: '/404', failOnStatusCode: false}).its('status').should('eq', 404)
  })
})
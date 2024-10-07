describe('Test Navigation', () => {
  it('passes', () => {
    //Test navigation links
    cy.visit('/')
    cy.url().should('include', '/')
    cy.visit('/about')
    cy.url().should('include', '/about')
    cy.visit('/portfolio')
    cy.url().should('include', '/portfolio')
    cy.visit('/blog')
    cy.url().should('include', '/blog')
    cy.visit('/contact')
    cy.url().should('include', '/contact')

    // Test login link
    cy.getDataCy('main-nav').within(() => {
      cy.getDataCy('dropdown-menu').click()
      cy.getDataCy('login-link').click()
    })

    // Test Register link
    cy.getDataCy('main-nav').within(() => {
      cy.getDataCy('dropdown-menu').click()
      cy.getDataCy('register-link').click()
    })

    // Test 404 works
    cy.request({url: '/404', failOnStatusCode: false}).its('status').should('eq', 404)
  })
})
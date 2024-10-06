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

    // Test Dropdown nav item works
    cy.contains('Login').should('not.be.visible')
    cy.getDataCy('top-nav').within(() => {
      cy.getDataCy('drop-down-nav').click()
    })
    cy.contains('Login').should('be.visible')
    cy.getDataCy('top-nav').within(() => {
      cy.getDataCy('drop-down-nav').click()
    })
    cy.contains('Login').should('not.be.visible')

    // Test Login and Register Links
    cy.getDataCy('top-nav').within(() => {
      cy.getDataCy('drop-down-nav').click()
      cy.getDataCy('login-button').click()
      cy.contains('Login').should('not.be.visible')
      cy.getDataCy('drop-down-nav').click()
      cy.getDataCy('register-button').click()
    })


    // Test 404 works
    cy.request({url: '/404', failOnStatusCode: false}).its('status').should('eq', 404)
  })
})
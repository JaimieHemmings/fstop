describe('test control panel functionality', () => {
  beforeEach(() => {
    cy.on("uncaught:exception", (e) => {
      console.log("error", e);
      return false;
      });
    cy.visit('/')
    cy.getDataCy('main-nav').within(() => {
      cy.getDataCy('dropdown-menu-profile').click()
      cy.getDataCy('login-link').click()
    })
    cy.get('form').within(() => {
      cy.get('[id=id_login]').type('testAdmin')
      cy.get('[id=id_password]').type('testPassword123')
      cy.get('[type=submit]').click()
    })
    cy.getDataCy('main-nav').within(() => {
      cy.getDataCy('dropdown-menu-profile').click()
      cy.getDataCy('admin').click()
    })
  })
  it('Has working valid links', () => {
    cy.on("uncaught:exception", (e) => {
      console.log("error", e);
      return false;
      });
    // Test links and ensure url is correct
    cy.contains('a', 'Messages').click()
    cy.url().should('include', '/control-panel/messages')
    cy.contains('a', 'Articles').click()
    cy.url().should('include', '/control-panel/articles')
    cy.contains('a', 'Payments').click()
    cy.url().should('include', '/control-panel/payments')
    cy.contains('a', 'Analytics').click()
    cy.url().should('include', '/control-panel/analytics')
    cy.contains('a', 'Home Page').click()
    cy.url().should('include', '/control-panel/homepage')
    cy.contains('a', 'About Page').click()
    cy.url().should('include', '/control-panel/about/edit')
    cy.contains('a', 'Services Page').click()
    cy.url().should('include', '/control-panel/services-pages')
    cy.contains('a', 'Portfolio Page').click()
    cy.url().should('include', '/control-panel/portfolio')
    cy.contains('a', 'Reviews').click()
    cy.url().should('include', '/control-panel/reviews')
    cy.contains('a', 'Main Site').click()
    cy.url().should('include', '/')
  })
});
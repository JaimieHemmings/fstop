describe('test homepage functionality', () => {
  beforeEach(() => {
    cy.setCookie('cookie-consent', 'accepted')
    cy.visit('/')
  })
  it('Has H1 with valid length and is visible', () => {
    cy.on("uncaught:exception", (e) => {
      console.log("error", e);
      return false;
      });
    // Test H1 exists with length greater than 0
    cy.get('h1')
      .should('exist')
      .and('be.visible')
      .should('have.length', 1)
      .invoke('text').should('have.length.gt', 0)
  })

  it('Has an accordian and functions correctly', () => {
    cy.on("uncaught:exception", (e) => {
      console.log("error", e);
      return false;
      });
    // Test accordion functionality
    cy.getDataCy('accordion').should('exist')
    cy.contains('Photography is a totally bespoke service').should('be.visible')
    cy.getDataCy('faq-item-3-heading').click()
    cy.contains('Photography is a totally bespoke service').should('not.be.visible')
    cy.contains('Yes, all of our photos are edited to ensure that they are of the highest quality').should('not.be.visible')
    cy.getDataCy('faq-item-4-heading').click()
    cy.contains('Yes, all of our photos are edited to ensure that they are of the highest quality').should('be.visible')
    cy.getDataCy('faq-item-6-heading').click()
  })
})
describe('test admin payments functionality', () => {
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
    cy.contains('a', 'Payments').click()
  })

  it('Has a table with payments', () => {
    cy.on("uncaught:exception", (e) => {
      console.log("error", e);
      return false;
      });
    // Test table exists and has payments
    cy.getDataCy('payments-table').should('exist')
    cy.getDataCy('payments-table').within(() => {
      cy.get('tr').should('have.length.gt', 1)
    })
  })

  it('Has a table with payments which can be viewed', () => {
    cy.on("uncaught:exception", (e) => {
      console.log("error", e);
      return false;
      });
    // Test table exists and has payments
    cy.getDataCy('payments-table').should('exist')
    cy.getDataCy('payments-table').within(() => {
      cy.get('tr').should('have.length.gt', 1)
      cy.get('tr').eq(1).within(() => {
        cy.contains('a', 'View').click()
      })
    })
    cy.url().should('include', '/control-panel/payments/')
  })

  it.only('Has functionality to create new payements', () => {
    cy.on("uncaught:exception", (e) => {
      console.log("error", e);
      return false;
      });
    cy.contains('a', 'Create New').click()
    cy.url().should('include', '/control-panel/payments/new')
    cy.get('form').within(() => {
      cy.get('[id=id_email]').type('testUser@gmail.com')
      cy.get('[id=id_amount]').type('100')
      cy.get('[type=submit]').click()
      cy.contains('This field is required.').should('be.visible')
    })
    // Cypress is currently incompatible with CKEditor so this requires additional testing manually - https://github.com/cypress-io/cypress/issues/26155
  })
})

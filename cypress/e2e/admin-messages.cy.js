describe('test control panel Messages functionality', () => {
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
    cy.contains('a', 'Messages').click()
  })
  it('Has a table with messages', () => {
    cy.on("uncaught:exception", (e) => {
      console.log("error", e);
      return false;
      });
    // Test table exists and has messages
    cy.getDataCy('messages-table').should('exist')
    cy.getDataCy('messages-table').within(() => {
      cy.get('tr').should('have.length.gt', 1)
    })
  })

  it('Has messages for which the status can be changed', () => {
    cy.on("uncaught:exception", (e) => {
      console.log("error", e);
      return false;
      });
    // Test table exists and has messages
    cy.getDataCy('messages-table').should('exist')
    cy.getDataCy('messages-table').within(() => {
      cy.get('tr').should('have.length.gt', 1)
      cy.get('tr').eq(1).within(() => {
        cy.contains('a', 'Mark Read').click()
      })
    })
    cy.contains('a', 'Mark Unread').click()
    cy.contains('Message status updated successfully').should('be.visible')
  })

  it('Has a table with messages which can be deleted', () => {
    cy.on("uncaught:exception", (e) => {
      console.log("error", e);
      return false;
      });
    // Test table exists and has messages
    cy.getDataCy('messages-table').should('exist')
    cy.getDataCy('messages-table').within(() => {
      cy.get('tr').should('have.length.gt', 1)
      cy.get('tr').eq(1).within(() => {
        cy.contains('a', 'Delete').click()
      })
    })
    cy.url().should('include', 'delete')  
    cy.contains('a', 'Delete').click()
    cy.contains('The item was deleted').should('be.visible')
    cy.contains('a', 'Return to dashboard').click()
    cy.url().should('include', '/control-panel/')  
  })
});
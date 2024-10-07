describe('Log in User Flow happy path', () => {
  beforeEach(() => {
    cy.visit('/')
    cy.getDataCy('main-nav').within(() => {
      cy.getDataCy('dropdown-menu').click()
      cy.getDataCy('login-link').click()
    })
  })

  it('passes', () => {
    cy.get('form').within(() => {
      cy.get('[id=id_login]').type('testAdmin')
      cy.get('[id=id_password]').type('testPassword123')
      cy.get('[type=submit]').click()
    })
    cy.contains('Successfully signed in as testAdmin.').should('be.visible')
  })

  it('fails gracefully', () => {
    cy.get('form').within(() => {
      cy.get('[id=id_login]').type('User1')
      cy.get('[id=id_password]').type('testPassword123')
      cy.get('[type=submit]').click()
    })
    cy.contains('The username and/or password you specified are not correct.').should('be.visible')

    cy.get('form').within(() => {
      cy.get('[id=id_login]').type('User1')
      cy.get('[type=submit]').click()
    })
    cy.get('[id=id_password]').then(($input) => {
      expect($input[0].validationMessage).to.eq('Please fill in this field.')
    })
  })
})
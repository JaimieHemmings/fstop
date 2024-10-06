describe('test homepage functionality', () => {
  beforeEach(() => {
    cy.visit('/contact')
  })
  it('Has H1 with valid length and is visible', () => {
    // Test H1 exists with length greater than 0
    cy.get('h1')
      .should('exist')
      .and('be.visible')
      .should('have.length', 1)
      .invoke('text').should('have.length.gt', 0)
  })

  it('Has a contact form which functions correctly', () => {
    // Test contact form functionality
    cy.getDataCy('contact-form').should('exist')
    cy.getDataCy('contact-form').within(() => {
      cy.get('[id=id_fname]').type('John')
      cy.get('[id=id_lname]').type('Doe')
      cy.get('[id=id_email]').type('test@test.com')
      cy.get('[id=id_message]').type('A string of text')
      cy.get('[type=submit]').click()
    })
  })

  it('Has a contact form which handles incorrect data correctly', () => {
    cy.getDataCy('contact-form').within(() => {
      cy.get('[id=id_fname]').type('3')
      cy.get('[id=id_email]').type('test@test')
      cy.get('[id=id_message]').type('f')
      cy.get('[type=submit]').click()
      cy.get('[id=id_lname]').then(($input) => {
        expect($input[0].validationMessage).to.eq('Please fill in this field.')
      })
      cy.get('[id=id_lname]').type('Doe')
      cy.get('[type=submit]').click()
      cy.contains("Enter a valid email address.").should('be.visible')
    })
  })
})
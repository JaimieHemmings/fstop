Cypress.Commands.add('getDataCy', (dataTestSelector) => {
  return cy.get(`[data-cy="${dataTestSelector}"]`);
});